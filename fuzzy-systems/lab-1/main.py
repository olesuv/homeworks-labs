import matplotlib.pyplot as plt


def calculate_median(height_stat: dict[int: list[float]]) -> dict[int: float]:
    for k in height_stat.keys():
        height_stat[k] = sum(height_stat[k]) / len(height_stat[k])

    max_v = max(height_stat.values())

    # Normalizing data. I no '1' in stat.
    if max_v != 1:
        for k, v in height_stat.items():
            height_stat[k] = float(format(float(v / max_v), ".2f"))

    return height_stat


def get_dict_keys(height_stat: dict[int: list[float]]) -> list[int]:
    heights: list[int] = []

    for k in height_stat.keys():
        heights.append(k)

    return heights


def get_dict_values(height_stat: dict[int: list[float]]) -> list[float]:
    medians: list[int] = []

    for v in height_stat.values():
        medians.append(v)

    return medians


def build_chart(height_list: list[int], medians_list: list[float]) -> None:
    plt.plot(height_list, medians_list)
    plt.title("Середнє значення зросту чоловіка")
    plt.savefig('output.png')


if __name__ == "__main__":
    height_dict = {
        150: [0, 0, 0, 0, 0, 0],              # 0
        155: [0.3, 0.2, 0.3, 0.1, 0.2, 0.2],  # 0.216
        160: [0.6, 0.4, 0.6, 0.3, 0.4, 0.5],  # 0.466
        165: [0.6, 0.5, 0.7, 0.5, 0.3, 0.6],  # 0.533
        170: [1, 0.9, 1, 0.7, 0.5, 1],        # 0.85
        175: [1, 1, 1, 1, 0.9, 1],            # 0.983
        180: [0.8, 0.6, 0.6, 1, 0.7, 0.5],    # 0.7
        185: [0.5, 0.3, 0.2, 0.4, 0.1, 0.2],  # 0.283
        190: [0.4, 0.2, 0.1, 0.3, 0.2, 0.1],  # 0.216
        195: [0.2, 0.3, 0.3, 0.2, 0.1, 0.1],  # 0.2
        200: [0, 0, 0, 0, 0, 0]               # 0
    }

    sample = calculate_median(height_dict)
    sample_k = get_dict_keys(sample)
    sample_v = get_dict_values(sample)

    print(sample)
    build_chart(sample_k, sample_v)
