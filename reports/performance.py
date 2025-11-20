

def generate_performance_report(data):
    groups = {}

    for row in data:
        position = row["position"]
        performance = float(row["performance"])

        if position not in groups:
            groups[position] = []

        groups[position].append(performance)

    result = []

    for position in groups:

        values = groups[position]
        avg_mean = sum(values) / len(values)
        result.append((position, avg_mean))

    def get_avg(item):
        return item[1]

    result = sorted(result, key=get_avg, reverse=True)

    return ["position", "avg_performance"], result
