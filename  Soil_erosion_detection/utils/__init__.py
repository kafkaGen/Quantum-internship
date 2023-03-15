from .dataset import SoilErosionDataset

import torch
import numpy as np
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

from settings.config import Config


def set_seed(seed):
    np.random.seed(seed)
    torch.manual_seed(seed)
    
    
def get_transforms(subset):
    if subset == 'train':
        transforms = A.Compose([
            A.Resize(height=Config.resize_to, width=Config.resize_to),
            #A.ColorJitter(),
            #A.RandomBrightnessContrast(),
            #A.HorizontalFlip(),
            #A.RandomResizedCrop(),
            #A.Rotate(),
            #A.ShiftScaleRotate(),
            #A.RGBShift(),
            #A.Blur(),
            #A.GaussNoise(),
            #A.ElasticTransform()
            A.Normalize(mean=Config.mean, std=Config.std),
            ToTensorV2(transpose_mask=True)
        ])
    else:
        transforms = A.Compose([
            A.Resize(height=Config.resize_to, width=Config.resize_to),
            A.Normalize(mean=Config.mean, std=Config.std),
            ToTensorV2(transpose_mask=True)
        ])
    
    return transforms


def get_shuffle(subset):
    if subset == 'train':
        return True
    else:
        return False