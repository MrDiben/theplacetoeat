function getInterval(
  intervals,
  startHour,
  startMin,
  endHour,
  stepHour,
  stepMin
) {
  for (let hour = startHour; hour < endHour; hour += stepHour) {
    for (let min = startMin; min < 60; min += stepMin) {
      let minutes = min.toString();
      let hours = hour.toString();
      if (minutes.length < 2) {
        minutes = `0${minutes.toString()}`;
      }
      if (hours.length < 2) {
        hours = `0${hours}`;
      }
      intervals.push(`${hours}:${minutes}`);
    }
  }
}

function getIntervals(start, end, stepHour, stepMin) {
  const intervals = [];
  const startHour = parseInt(start.substring(0, 2));
  const startMin = parseInt(start.substring(3, 5));
  let endHour = parseInt(end.substring(0, 2));

  // Case when restaurant is opened 24/24
  if (startHour === endHour && startHour === 0 && endHour === 0) {
    endHour = 24;
  }

  // Case when starthour > endHour
  if (startHour > endHour) {
    this.getInterval(intervals, startHour, startMin, 24, stepHour, stepMin);
    this.getInterval(intervals, 0, startMin, endHour, stepHour, stepMin);
  } else {
    this.getInterval(
      intervals,
      startHour,
      startMin,
      endHour,
      stepHour,
      stepMin
    );
  }
  // getInterval()
  return intervals;
}

export default { getIntervals, getInterval };
