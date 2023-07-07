import re
import random
import string


def get_colors_from_html(html):
    colors = re.findall(r'\b\w+\b', html)
    return colors

def get_mean_color(colors):
    counts = {}
    for color in colors:
        if color not in counts:
            counts[color] = 0
        counts[color] += 1
    total = sum(counts.values())
    mean = 0
    for color, count in counts.items():
        mean += color * count / total
    return mean

def get_most_common_color(colors):
    counts = {}
    for color in colors:
        if color not in counts:
            counts[color] = 0
        counts[color] += 1
    max_count = 0
    max_color = None
    for color, count in counts.items():
        if count > max_count:
            max_count = count
            max_color = color
    return max_color

def get_median_color(colors):
    colors.sort()
    median = len(colors) // 2
    if len(colors) % 2 == 0:
        median = (colors[median - 1] + colors[median]) / 2
    else:
        median = colors[median]
    return median

def get_variance(colors):
    mean = get_mean_color(colors)
    variance = 0
    for color in colors:
        variance += (color - mean)**2
    variance /= len(colors)
    return variance

def get_probability_of_red(colors):
    count_red = 0
    for color in colors:
        if color == 'red':
            count_red += 1
    return count_red / len(colors)

def save_colors_and_frequencies_to_postgresql(colors, frequencies):
    import psycopg2
    conn = psycopg2.connect(
        host='localhost',
        database='bincom',
        user='postgres',
        password='my_bincom_password')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS colors (color text, frequency integer)')
    for color, frequency in frequencies.items():
        cur.execute('INSERT INTO colors (color, frequency) VALUES (%s, %s)', (color, frequency))
    conn.commit()

def main():
    html = open('dresses.html', 'r').read()
    colors = get_colors_from_html(html)
    mean = get_mean_color(colors)
    most_common = get_most_common_color(colors)
    median = get_median_color(colors)
    variance = get_variance(colors)
    probability_of_red = get_probability_of_red(colors)
    print('Mean color:', mean)
    print('Most common color:', most_common)
    print('Median color:', median)
    print('Variance:', variance)
    print('Probability of red:', probability_of_red)

if __name__ == '__main__':
    main()
