# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

"""Benchmark script for TensorFlow.

See the README for more information.
"""

from __future__ import print_function


import tensorflow as tf

import benchmark_cnn
import cnn_util
from cnn_util import log_fn

from setenvs import setenvs
from setenvs import arglist
import sys
args = arglist()

benchmark_cnn.define_flags()


def main(extra_flags):
  # extra_flags is a list of command line arguments, excluding those defined
  # in tf.flags.FLAGS. extra_flags[0] is always the program name. It is an error
  # to supply flags not defined with tf.flags.FLAGS, so we raise an ValueError
  # in that case.
  assert len(extra_flags) >= 1
  # if len(extra_flags) > 1:
    # raise ValueError('Received unknown flags: %s' % extra_flags[1:])

  global args
  args = setenvs(sys.argv)
  print('Running on CPU :', args.cpu)

  params = benchmark_cnn.make_params_from_flags()
  benchmark_cnn.setup(params)
  bench = benchmark_cnn.BenchmarkCNN(params)

  tfversion = cnn_util.tensorflow_version_tuple()
  log_fn('TensorFlow:  %i.%i' % (tfversion[0], tfversion[1]))

  bench.print_info()
  bench.run()


if __name__ == '__main__':
  tf.app.run()
