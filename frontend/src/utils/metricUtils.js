// ----------------------------------------
// Convert a financial value into a number
// ----------------------------------------

export function parseMetricValue(value) {

    if (
        value === null ||
        value === undefined ||
        value === "" ||
        value === "—" ||
        value === "."
    ) {
        return null;
    }

    let cleaned = value.toString().trim();

    // Remove commas
    cleaned = cleaned.replace(/,/g, "");

    const multiplier = cleaned.slice(-1).toUpperCase();

    let number = parseFloat(cleaned);

    if (isNaN(number)) {
        return null;
    }

    switch (multiplier) {

        case "K":
            number *= 1e3;
            break;

        case "M":
            number *= 1e6;
            break;

        case "B":
            number *= 1e9;
            break;

        case "T":
            number *= 1e12;
            break;

        default:
            break;
    }

    return number;

}

// ----------------------------------------
// Find highest value
// ----------------------------------------

export function getHighestValue(values) {

    const numbers = values
        .map(parseMetricValue)
        .filter(value => value !== null);

    if (numbers.length === 0) {
        return null;
    }

    return Math.max(...numbers);

}

// ----------------------------------------
// Find lowest value
// ----------------------------------------

export function getLowestValue(values) {

    const numbers = values
        .map(parseMetricValue)
        .filter(value => value !== null);

    if (numbers.length === 0) {
        return null;
    }

    return Math.min(...numbers);

}

// ----------------------------------------
// Determine cell class
// ----------------------------------------

export function getMetricClass(value, highest, lowest) {

    const parsed = parseMetricValue(value);

    if (parsed === null) {
        return "metric-missing";
    }

    if (parsed === highest) {
        return "metric-highest";
    }

    if (parsed === lowest) {
        return "metric-lowest";
    }

    return "";

}