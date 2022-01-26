N_EPOCHS = 1
N_EPOCHS_DECAY = 0

if __name__ == '__main__':
  params = {
    'N_EPOCHS':N_EPOCHS,
    'N_EPOCHS_DECAY':N_EPOCHS_DECAY
  }
  with open('.env', 'w+') as f:
    for param in params:
      f.write(f'export {param}={params[param]}\n')