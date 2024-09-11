import torch.nn            as nn
import torchvision.models as models

class ModifiedEfficientNet(nn.Module):
    def __init__(self, num_classes=1):
        super(ModifiedEfficientNet, self).__init__()
        
        # Load a pre-trained EfficientNet model
        self.efficientnet = models.efficientnet_v2_s(weights='EfficientNet_V2_S_Weights.IMAGENET1K_V1')
        
        # Get the number of input features for the final fully connected layer
        num_features = self.efficientnet.classifier[1].in_features
        
        # Replace the fully connected layer with a new one that has the desired number of output classes
        self.efficientnet.classifier = nn.Sequential(
            nn.Linear(num_features, num_classes)
        )

    def forward(self, x, return_feature_maps=False):
        # Forward pass through the EfficientNet
        if return_feature_maps:
            feature_maps = []
            for name, layer in self.efficientnet.features._modules.items():
                x = layer(x)
                feature_maps.append(x)  # Store the feature map after this layer
            return feature_maps
        else:
            x = self.efficientnet(x)  # Final output
            return x
    
    def extract_features(self, x):
        # Extract features before the classifier layer
        x = self.efficientnet.features(x)
        x = self.efficientnet.avgpool(x)
        x = torch.flatten(x, 1)
        
        return x
