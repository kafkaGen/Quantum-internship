import torch


class Config():
    # Training
    seed = 13
    min_epochs = 5
    max_epochs = 25
    learning_rate = 0.001
    num_classes = 1
    device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')
    accelerator = 'gpu' if torch.cuda.is_available() else 'cpu'
    
    # Data preparation
    data_path = 'data'
    model_path = 'models'
    logs_path = '.'
    batch_size = 4
    num_workers = 4
    
    # Data transformation
    mean = (0.485, 0.456, 0.406)
    std = (0.229, 0.224, 0.225)
    resize_to = 256
    mean = 0.5
    std = 0.5