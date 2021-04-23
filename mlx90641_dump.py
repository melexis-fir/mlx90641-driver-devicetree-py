from mlx90641_devicetree import *
from mlx90641 import *


def main():
    print("start")
    dev = MLX90641()
    print("dev", dev)

    r = dev.i2c_init("/dev/i2c-1")
    # r = dev.i2c_init("ftdi://ftdi:2232/1")
    # r = dev.i2c_init("mcp://mcp:2221/0")
    print("init", r)
    r = dev.set_refresh_rate(1)
    print("setRefreshRate", r)

    refresh_rate = dev.get_refresh_rate()
    print("refresh rate: {}".format(refresh_rate))

    dev.dump_eeprom()
    dev.extract_parameters()

    for i in range(0, 10):
        dev.get_frame_data()
        ta = dev.get_ta() - 5.0
        emissivity = 1

        to = dev.calculate_to(emissivity, ta)

        print("{:02d}: {}".format(i, ','.join(format(x, ".2f") for x in to)))


if __name__ == "__main__":
    main()
