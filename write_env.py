import yaml

if __name__ == '__main__':
  
  with open('params.yaml', 'r') as stream:
    params = yaml.safe_load(stream)

  with open('.env', 'w+') as f:
    for param in params:
      f.write(f'export {param}={params[param]}\n')
