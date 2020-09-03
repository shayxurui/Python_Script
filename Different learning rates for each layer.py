import torch
import torchvision

net=torchvision.models.AlexNet()

# print(net)

features_paras=net.features.parameters()
classifier_paras=net.classifier.parameters()

optimizer = torch.optim.Adam([
    {'params':features_paras,'lr':0.001,'weight_decay':0.001},
    {'params':classifier_paras,'lr':0.01,'weight_decay':0.01},
]
)

print(optimizer)