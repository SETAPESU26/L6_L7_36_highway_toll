
def parse_plate(plate):
    if not isinstance(plate, str):
        return None

    parts = plate.strip().split('-')

    if len(parts) != 4:
        return None

    state, district, series, number = parts

    if not (len(state) == 2 and state.isalpha()):
        return None

    if not (district.isdigit() and series.isalpha() and number.isdigit()):
        return None

    if not (1 <= len(district) <= 2 and 1 <= len(series) <= 3 and 1 <= len(number) <= 4):
        return None

    return state.upper(), int(district), int(number)


def trip_cost(text):
    if not isinstance(text, str):
        return None

    parts = text.lower().split('x')

    if len(parts) != 2:
        return None

    count, rate = parts

    if not (count.strip().isdigit() and rate.strip().isdigit()):
        return None

    count = int(count)
    rate = int(rate)

    if count <= 0:
        return None

    return count * rate


def axle_class(axles):
    if not isinstance(axles, (str, int)) or isinstance(axles, bool):
        return None

    try:
        n = int(axles)
    except (ValueError, TypeError):
        return None

    if isinstance(axles, str) and not axles.strip().isdigit():
        return None

    if n < 2:
        return None

    if n == 2:
        return 'car'

    if n <= 4:
        return 'truck'

    return 'heavy'


def main():
    print("==== Running parse_plate ====")
    user_input = input("Enter a plate (e.g. KA-05-AB-1234): ")
    result = parse_plate(user_input)
    print("State, District and Number:", result if result is not None else "Invalid plate")

    print("\n==== Running trip_cost ====")
    user_input = input("Enter trips x rate (e.g. 3x150): ")
    result = trip_cost(user_input)
    print("Trip Cost:", result if result is not None else "Invalid trip cost input")

    print("\n==== Running axle_class ====")
    user_input = input("Enter an axle count (e.g. 3): ")
    result = axle_class(user_input)
    print("Vehicle Class:", result if result is not None else "Invalid axle count")


if __name__ == "__main__":
    main()
