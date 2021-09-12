export function getDayDifference(secondDate: Date): number {
  const oneDay: number = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
    const firstDate: Date = new Date (Date.now());

  const diffDays = Math.round(Math.abs((+firstDate - +secondDate) / oneDay));

  return diffDays;
}
