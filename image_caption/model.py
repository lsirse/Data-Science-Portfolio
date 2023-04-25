import torch
import torch.nn as nn
import torchvision.models as models


class EncoderCNN(nn.Module):
    def __init__(self, embed_size):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        for param in resnet.parameters():
            param.requires_grad_(False)
        
        modules = list(resnet.children())[:-1]
        self.resnet = nn.Sequential(*modules)
        self.embed = nn.Linear(resnet.fc.in_features, embed_size)

    def forward(self, images):
        features = self.resnet(images)
        features = features.view(features.size(0), -1)
        features = self.embed(features)
        return features
    

    
    
class DecoderRNN(nn.Module):
    
    def __init__(self, embed_size, hidden_size, vocab_size, batch_size, drop_prob = 0.2, num_layers=1):
        super(DecoderRNN, self).__init__()

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.embed_size = embed_size
        self.hidden_size = hidden_size
        self.vocab_size = vocab_size
        self.num_layers = num_layers
        self.batch_size = batch_size
        
        self.embedding = nn.Embedding(vocab_size, embed_size)
        
        self.lstm = nn.LSTM(embed_size, hidden_size, num_layers,
                            dropout=drop_prob, batch_first=True)
        
        self.fc = nn.Linear(hidden_size, vocab_size)
        
    def forward(self, features, captions):
        
        captions_embedding = self.embedding(captions[: , :-1])
        
        features = features.unsqueeze(1)
        
        inputs = torch.cat([features, captions_embedding], 1)
        
        x, _ = self.lstm(inputs)
        
        x = self.fc(x)
        
        return x
    
    def sample(self, inputs, states=None, max_len=20):
        " accepts pre-processed image tensor (inputs) and returns predicted sentence (list of tensor ids of length max_len) "
        result = []
        
        for _ in range(max_len):
            output, states = self.lstm(inputs, states)
            
            output = output.squeeze(1)
            output = self.fc(output)
            r = output.max(1)[1]
            
            result.append(r.item())
            
            # Prepare the new input of the lstm
            inputs = self.embedding(r).unsqueeze(1)
        
        return result