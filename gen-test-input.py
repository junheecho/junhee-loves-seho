from collections.abc import Sequence
from tqdm import tqdm
import os

from absl import app
from absl import flags

FLAGS = flags.FLAGS

flags.DEFINE_string('destination', 'test-input/', 'Directory to save test input files.')
flags.DEFINE_float('size', 0.01, 'File size in GB.')
flags.DEFINE_integer('num_files', 3, 'Number of files.')


def main(argv: Sequence[str]) -> None:
  if len(argv) > 1:
    raise app.UsageError('Too many command-line arguments.')

  os.makedirs(FLAGS.destination, exist_ok=True)
  for i in range(FLAGS.num_files):
    print(f'{i}.txt')
    with open(FLAGS.destination + f'/{i}.txt', 'w') as f:
      f.write('{')
      # 1MB
      content = f'{chr(ord("a") + i)}' * 1024 * 1024
      for j in tqdm(range(int(FLAGS.size * 1024))):
        f.write(content)
      f.write('}')


if __name__ == '__main__':
  app.run(main)

