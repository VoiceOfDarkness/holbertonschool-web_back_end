/* eslint-disable */

export default function cleanSet(set, startString) {
  if (startString === "") return "";

  const filteredValues = Array.from(set)
    .filter((value) => value.startsWith(startString))
    .map((value) => value.slice(startString.length));

  const cleanedString = filteredValues.join("-");
  return cleanedString;
}
