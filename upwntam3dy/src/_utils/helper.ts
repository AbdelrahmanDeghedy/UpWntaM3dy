export function getDayDifference(secondDate: Date): number {
  const oneDay: number = 24 * 60 * 60 * 1000; // hours*minutes*seconds*milliseconds
    const firstDate: Date = new Date (Date.now());

  const diffDays = Math.round(Math.abs((+firstDate - +secondDate) / oneDay));

  return diffDays;
}

export function randomIdGenerator() {
  const S4 = function() {
     return (((1+Math.random())*0x10000)|0).toString(16).substring(1);
  };
  return (S4()+S4()+"-"+S4()+"-"+S4()+"-"+S4()+"-"+S4()+S4()+S4());
}