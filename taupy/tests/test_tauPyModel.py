from unittest import TestCase

__author__ = 'nicolas'
import os


class TestTauPyModel(TestCase):
    def test_create_taup_model(self):
        """
        See if the create model function in the tau interface runs smoothly.
        """
        from taupy import tau
        try:
            os.remove("ak135.taup")
        except FileNotFoundError:
            pass
        ak135 = tau.TauPyModel("ak135", taup_model_path=".")
        os.remove("ak135.taup")