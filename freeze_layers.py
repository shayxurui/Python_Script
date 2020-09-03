import torch
import torchvision

net=torchvision.models.alexnet()

# net.to(device)

print(net)

for para in net.features.parameters():       #冻结nn.Sequential的所有层
    para.requires_grad = False


# net.classifier.fc.weight.requires_grad=False       #冻结某一层

# print(net.classifier.fc.weight.requires_grad)        #查看是否冻结该层参数

optimizer=torch.optim.Adam(filter(lambda p: p.requires_grad, net.parameters()),lr=0.0001)   #优化器过滤不需要更新层的参数

for para in net.features.parameters():       #解冻nn.Sequential的所有层
    para.requires_grad = True

optimizer.add_param_group({'params': net.features.parameters()})     #将解冻后的参数加入到优化器中