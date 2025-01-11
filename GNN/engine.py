import torch
import torch.nn as nn
from sklearn.metrics import r2_score


class EnginehERG:
    def __init__(self, model, optimizer, device):
        self.model = model
        self.device = device
        self.optimizer = optimizer

    @staticmethod
    def loss_fn(targets, outputs):
        return nn.MSELoss()(outputs, targets)

    def train(self, data_loader):
        self.model.train()
        final_loss = 0
        for data in data_loader:
            data = data.to(self.device)
            self.optimizer.zero_grad()
            outputs = self.model(data.x, data.edge_attr, data.edge_index, data.batch)
            loss = self.loss_fn(data.y.unsqueeze(1), outputs)
            loss.backward()
            self.optimizer.step()
            final_loss += loss.item()

        return final_loss / len(data_loader)

    def validate(self, data_loader):
        self.model.eval()
        final_loss = 0
        r2_total = 0
        with torch.no_grad():
            for data in data_loader:
                data = data.to(self.device)
                outputs = self.model(data.x, data.edge_attr, data.edge_index, data.batch)
                loss = self.loss_fn(data.y.unsqueeze(1), outputs)
                final_loss += loss.item()

                r2 = r2_score(data.y.unsqueeze(1).to("cpu").detach().numpy(), outputs.to("cpu").detach().numpy())
                r2_total += r2

        mse = final_loss / len(data_loader)
        
        return mse, r2_total / len(data_loader)

    def test(self, data_loader):
        self.model.eval()
        final_loss = 0
        r2_total = 0
        with torch.no_grad():
            for data in data_loader:
                data = data.to(self.device)
                outputs = self.model(data.x, data.edge_attr, data.edge_index, data.batch)
                loss = self.loss_fn(data.y.unsqueeze(1), outputs)
                final_loss += loss.item()

                r2 = r2_score(data.y.unsqueeze(1).to("cpu").detach().numpy(), outputs.to("cpu").detach().numpy())
                r2_total += r2

        mse = final_loss / len(data_loader)
        return mse, r2_total / len(data_loader)