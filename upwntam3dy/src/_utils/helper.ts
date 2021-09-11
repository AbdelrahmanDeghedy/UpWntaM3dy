export function getDayDifference(firstDate: Date, secondDate: Date): number {
  const oneDay: number = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
  //   const firstDate: Date = new Date(2008, 1, 12);

  const diffDays = Math.round(Math.abs((+firstDate - +secondDate) / oneDay));

  return diffDays;
}
