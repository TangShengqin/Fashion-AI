#-*-coding:utf-8-*-
import torch
import torchvision
import torch.nn as nn
import torch.nn.functional as F
# import pretrainedmodels  # for pytorch v0.4 python 3.5


class Modified_densenet201(nn.Module):
    """docstring for ClassName"""
    def __init__(self, num_classs=100, input_size=224):
        super(Modified_densenet201, self).__init__()
        model = torchvision.models.densenet201(pretrained=True)
        self.num_classs = num_classs
        self.input_size = input_size
        if input_size==224:
            self.avgpool_size = 7 # for 224x224 input
        elif input_size==448:
            self.avgpool_size = 14 # for 448x448 input
        for i, m in enumerate(model.children()):
            if i==0:
                self.features = m
            else:
                self.classifier = nn.Linear(in_features=1920, out_features=num_classs)

    def forward(self, x):
        features = self.features(x)
        out = F.relu(features, inplace=True)
        out = F.avg_pool2d(out, kernel_size=self.avgpool_size).view(features.size(0), -1)
        out = self.classifier(out)
        return out

class Modified_Resnet50(nn.Module):
    """docstring for ClassName"""
    def __init__(self, num_classs=100, input_size=224):
        super(Modified_Resnet50, self).__init__()
        model = torchvision.models.resnet50(pretrained=True)
        self.num_classs = num_classs
        if input_size==224:
            self.avgpool_size = 7
        elif input_size==448:
            self.avgpool_size = 14
        temp = []
        for i, m in enumerate(model.children()):
            if i<=7:
                temp.append(m)
            elif i==8:
                temp.append(nn.AvgPool2d(kernel_size=self.avgpool_size, stride=1, padding=0, ceil_mode=False, count_include_pad=True))
            else:
                self.classifier = nn.Linear(in_features=2048, out_features=num_classs)
        self.features = nn.Sequential(*temp)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

class Modified_Resnet101(nn.Module):
    """docstring for ClassName"""
    def __init__(self, num_classs=100, input_size=224):
        super(Modified_Resnet101, self).__init__()
        model = torchvision.models.resnet101(pretrained=True)
        self.num_classs = num_classs
        if input_size==224:
            self.avgpool_size = 7
        elif input_size==448:
            self.avgpool_size = 14
        temp = []
        for i, m in enumerate(model.children()):
            if i<=7:
                temp.append(m)
            elif i==8:
                temp.append(nn.AvgPool2d(kernel_size=self.avgpool_size, stride=1, padding=0, ceil_mode=False, count_include_pad=True))
            else:
                self.classifier = nn.Linear(in_features=2048, out_features=num_classs)
        self.features = nn.Sequential(*temp)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

class Modified_Resnet152(nn.Module):
    """docstring for ClassName"""
    def __init__(self, num_classs=100, input_size=224):
        super(Modified_Resnet152, self).__init__()
        model = torchvision.models.resnet152(pretrained=True)
        self.num_classs = num_classs
        if input_size==224:
            self.avgpool_size = 7
        elif input_size==448:
            self.avgpool_size = 14
        temp = []
        for i, m in enumerate(model.children()):
            if i<=7:
                temp.append(m)
            elif i==8:
                temp.append(nn.AvgPool2d(kernel_size=self.avgpool_size, stride=1, padding=0, ceil_mode=False, count_include_pad=True))
            else:
                self.classifier = nn.Linear(in_features=2048, out_features=num_classs)
        self.features = nn.Sequential(*temp)

    def forward(self, x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

# for pytorch v0.4 python 3.5
class Modified_nasnetalarge(object):
    """docstring for ClassName"""
    def __init__(self, num_classs=100):
        super(Modified_nasnetalarge, self).__init__()
        self.num_classs = num_classs
        model = pretrainedmodels.__dict__[model_name](num_classes=1000, pretrained='imagenet')
        temp = []
        for i,m in enumerate(model.children()):
            if i<=25:
                temp.append(m)
            else:
                self.classifier = nn.Linear(in_features=4032, out_features=num_classs)
        self.features = nn.Sequential(*temp)

    def forward(x):
        x = self.features(x)
        x = x.view(x.size(0), -1)
        x = self.classifier(x)
        return x

