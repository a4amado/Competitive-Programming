let myDay = new Date().getDay();
switch (myDay) {
    default:
        myDay = 'Unknown';
        break;
    case 0:
        myDay = 'Sunday';
        break;
    case 1:
        myDay = 'Monday';
        break;
    case 2:
        myDay = 'Tuesday';
        break;
    case 3:
        myDay = 'Wednesday';
        break;
    case 4:
        myDay = 'Thursday';
        break;
    case 5:
        myDay = 'Friday';
        break;
    case 6:
        myDay = 'Saturday';
        break;
};
console.log(myDay);