import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

from src.pipeline import predict_pipeline
from src.utils import save_object, load_object


class PredictionPathTests(unittest.TestCase):
    def test_prediction_resolves_artifacts_from_project_not_working_directory(self):
        old_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            fake_module = root / 'project/src/pipeline/predict_pipeline.py'
            artifacts = root / 'project/artifacts'
            x = np.array([[0.0], [1.0], [2.0]])
            scaler = StandardScaler().fit(x)
            model = LinearRegression().fit(scaler.transform(x), [1.0, 3.0, 5.0])
            save_object(str(artifacts / 'model.pkl'), model)
            save_object(str(artifacts / 'preprocessor.pkl'), scaler)
            try:
                os.chdir(root)
                with patch.object(predict_pipeline, '__file__', str(fake_module)):
                    result = predict_pipeline.PredictPipeline().predict([[3.0]])
                np.testing.assert_allclose(result, [7.0])
            finally:
                os.chdir(old_cwd)

    def test_save_object_accepts_current_directory_filename(self):
        old_cwd = os.getcwd()
        with tempfile.TemporaryDirectory() as directory:
            try:
                os.chdir(directory)
                save_object('model.pkl', {'saved': True})
                self.assertEqual(load_object('model.pkl'), {'saved': True})
            finally:
                os.chdir(old_cwd)


if __name__ == '__main__':
    unittest.main()
