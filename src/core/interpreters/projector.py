from core.interpreters.base import BaseInterpreter
from core.interpreters.interpreter_signature import InterpreterSignature
from typing import cast
import torch.nn as nn
import torch.optim as optim

class Projector(BaseInterpreter):
    class AutoEncoder( nn.Module ):
        def __init__( self, input: int, latent: int  ):
            super( Projector.AutoEncoder, self ).__init__()
            self.encoder = nn.Sequential(
                nn.Linear(input, 128),
                nn.ReLU(),
                nn.Linear(128, 64),
                nn.ReLU(),
                nn.Linear(64, latent)
            )
            self.decoder = nn.Sequential(
                nn.Linear(latent, 64),
                nn.ReLU(),
                nn.Linear(64, 128),
                nn.ReLU(),
                nn.Linear(128, input)
            )
        def forward( self, X ):
            return self.decoder( self.encoder( X ) )

    def __init__(self, name, signature: InterpreterSignature):
        super().__init__(name, signature)
        self._autoencoders = {}

    def run(self, config, models, dataset, selection):
        if isinstance(self._autoencoders.get( dataset ), Projector.AutoEncoder ):
            embedings = cast( Projector.AutoEncoder, self._autoencoders.get( dataset ))(dataset.select( selection ))
            return { 'embeddings': embedings }
        else:
            autoencoder = Projector.AutoEncoder( 784, 32 )
            criterion = nn.MSELoss()
            optimizer = optim.Adam( autoencoder.parameters(), lr=0.001)
            epochs = 10
            for epoch in range( epochs ):
                for data in dataset:
                    optimizer.zero_grad()
                    output = autoencoder( data )
                    loss = criterion( output, data )
                    loss.backwards()
                    optimizer.step()
            self._autoencoders[dataset] = autoencoder
            return self.run( config, models, dataset, selection )
