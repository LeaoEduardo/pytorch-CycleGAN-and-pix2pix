import sys

if __name__ == '__main__':
  with open(sys.argv[1], 'r+') as logfile:
    lines = logfile.readlines()

  with open(f"{sys.argv[2]}_loss.csv", "w+") as metricsfile:
    metricsfile.write("epoch, iters, G_GAN, G_L1, D_real, D_fake\n")
    for line in lines[1:]:
      new_line = line.replace(",","").strip("()")
      words = new_line.split()
      metricsfile.write(f"{int(words[1])}, {int(words[3])}, {float(words[9])}, {float(words[11])}, {float(words[13])}, {float(words[15])}\n")