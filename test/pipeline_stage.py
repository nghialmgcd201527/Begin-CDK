import builtins
import typing
from constructs import Construct
from aws_cdk import (
    Stage
)
from .test_stack import TestStack

class WorkshopPipelineStage(Stage):

    def __init__(self, scope: Construct, id: str, **kwargs):
        super().__init__(scope, id, **kwargs)

        service = TestStack(self, 'WebService')