import moment from "moment";

interface dateTimeConfigObjectInterface {
  includeDay ?: boolean;
  includeMonth ?: boolean;
  includeYear ?: boolean;
  abbreviatedYear ?: boolean;

  includeHour ?: boolean;
  includeMinute ?: boolean;
  includeSecond ?: boolean;

  timeFirst ?: boolean;
  
  dateSeparator ?: string;
  timeSeparator ?: string;
  dateTimeSeparator ?: string;

  dateCombination ?: string;
  timeCombination ?: string;

  twelveHourSystem ?: boolean;
  amPmLetter?: boolean;

  local?: boolean;

  startOf ?: string;
  endOf ?: string;

  add ?: [number, string];
  subtract ?: [number, string];

  shortMonthName ?: boolean;
  longMonthName ?: boolean;

  shortDayName ?: boolean,
  longDayName ?: boolean,

  utcTime ?: boolean;

  endbleValueOf ?: boolean;
  endbleToDate ?: boolean;
  endbleFromNow ?: boolean;

  formatString ?: string;
}

export class DateFormatter {
  private timeDateUnformatted : string | undefined;
  private config : dateTimeConfigObjectInterface;
  
  constructor(timeDateUnformatted: string, config : dateTimeConfigObjectInterface = {
    includeDay: true,
    includeMonth: true,
    includeYear: true,
    includeHour : true,
    includeMinute : true,
    includeSecond : false,
    timeFirst: true,
    dateSeparator: "/",
    timeSeparator : ":",
    dateTimeSeparator : " - ",
    dateCombination : "dmy", 
    abbreviatedYear : false,
    timeCombination : "hms",
    twelveHourSystem : true,
    amPmLetter: true,
    local: true,
    startOf : "",
    endOf : "",
    add : [0, "d"],
    subtract : [0, "d"],
    shortMonthName : false,
    longMonthName : false,
    utcTime : false,
    endbleValueOf : false,
    endbleToDate: false,
    endbleFromNow: false,
    formatString : "",
  }) {
    
    this.timeDateUnformatted = timeDateUnformatted === "" ? undefined : timeDateUnformatted;
    this.config = config;
    
    this.config.timeFirst = this.config.timeFirst !== undefined ? this.config.timeFirst : true;
    this.config.includeDay = this.config.includeDay !== undefined ? this.config.includeDay : true;
    this.config.includeMonth = this.config.includeMonth !== undefined ? this.config.includeMonth : true;
    this.config.includeYear = this.config.includeYear !== undefined ? this.config.includeYear : true;
    this.config.abbreviatedYear = this.config.abbreviatedYear !== undefined ? this.config.abbreviatedYear : false;
    
    this.config.includeHour = this.config.includeHour !== undefined ? this.config.includeHour : true;
    this.config.includeMinute = this.config.includeMinute !== undefined ? this.config.includeMinute : true;
    this.config.includeSecond = this.config.includeSecond !== undefined ? this.config.includeSecond : false;
    
    this.config.dateSeparator = this.config.dateSeparator !== undefined ? this.config.dateSeparator : "/";
    this.config.timeSeparator = this.config.timeSeparator !== undefined ? this.config.timeSeparator : ":";
    this.config.dateTimeSeparator = this.config.dateTimeSeparator !== undefined ? this.config.dateTimeSeparator : " - ";
    
    this.config.dateCombination = this.config.dateCombination !== undefined ? this.config.dateCombination : "dmy";
    this.config.timeCombination = this.config.timeCombination !== undefined ? this.config.timeCombination : "hms";
    
    this.config.twelveHourSystem = this.config.twelveHourSystem !== undefined ? this.config.twelveHourSystem : true;
    this.config.amPmLetter = this.config.amPmLetter !== undefined ? this.config.amPmLetter : true;
    
    this.config.local = this.config.local !== undefined ? this.config.local : true;
    
    this.config.startOf = this.config.startOf !== undefined ? this.config.startOf : "";
    this.config.endOf = this.config.endOf !== undefined ? this.config.endOf : "";
    
    this.config.add = this.config.add !== undefined ? this.config.add : [0, "d"];
    this.config.subtract = this.config.subtract !== undefined ? this.config.subtract : [0, "d"];
    
    this.config.shortMonthName = this.config.shortMonthName !== undefined ? this.config.shortMonthName : false;
    this.config.longMonthName = this.config.longMonthName !== undefined ? this.config.longMonthName : false;
    
    this.config.shortDayName = this.config.shortDayName !== undefined ? this.config.shortDayName : false;
    this.config.longDayName = this.config.longDayName !== undefined ? this.config.longDayName : false;
    
    this.config.utcTime = this.config.utcTime !== undefined ? this.config.utcTime : false;
    
    this.config.endbleValueOf = this.config.endbleValueOf !== undefined ? this.config.endbleValueOf : false;
    this.config.endbleToDate = this.config.endbleToDate !== undefined ? this.config.endbleToDate : false;
    this.config.endbleFromNow = this.config.endbleFromNow !== undefined ? this.config.endbleFromNow : false;
    
    this.config.formatString = this.config.formatString !== undefined ? this.config.formatString : "";
  
  }

  // Creates the format string that will be passed to the moment utc method 
  private createFormatString (type: string) {
    if (this.config.formatString !== "") {
      return this.config.formatString;
    }

    let  monthPattern = "MM";
    if (this.config.shortMonthName || this.config.longMonthName) {
      monthPattern = this.config.shortMonthName ? "MMM" : "MMMM";
    }

    let  dayPattern = "DD";
    if (this.config.shortDayName || this.config.longDayName) {
        dayPattern = this.config.shortDayName ? "ddd" : "dddd";
    }

    const dateDic = {
      "d" : [dayPattern, this.config.includeDay],
      "m" : [monthPattern, this.config.includeMonth],
      "y" : [this.config.abbreviatedYear ? "YY" : "YYYY", this.config.includeYear]
    };

    const timeDic = {
      "h" : [this.config.twelveHourSystem ? "hh" : "HH", this.config.includeHour],
      "m" : ["mm", this.config.includeMinute],
      "s" : ["ss", this.config.includeSecond],
    };

    const usedDic = type === "date" ? dateDic : timeDic;
    const usedCombination = type === "date" ? this.config.dateCombination : this.config.timeCombination;
    const usedSeparator = type === "date" ? this.config.dateSeparator: this.config.timeSeparator;


    const firstItem = usedDic[usedCombination[0]];
    const middleItem = usedDic[usedCombination[1]];
    const lastItem = usedDic[usedCombination[2]];

    const formatString = `${firstItem[1] ? firstItem[0] : ""}${
      firstItem[1] && middleItem[1] ? usedSeparator : ""
    }${middleItem[1] ? middleItem[0] : ""}${
      firstItem[1] && lastItem[1] && middleItem[1] === false ? usedSeparator : ""
    }${
      middleItem[1] && lastItem[1] ? usedSeparator : ""
    }${lastItem[1] ? lastItem[0] : ""}${this.config.amPmLetter && type === "time" ? " A" : ""}`;

    return formatString;
  }

  private applyMomemntMethods (formatString : string) : string {
    let localTime : any =  this.config.utcTime ? moment.utc(this.timeDateUnformatted) : moment(this.timeDateUnformatted).utc();
    
    if (this.config.local) {
      localTime = localTime
      .local()
    }

    if (this.config.startOf !== "") {
      localTime = localTime.startOf (this.config.startOf);      
    }

    if (this.config.endOf !== "") {
      localTime = localTime.endOf (this.config.endOf);      
    }

    if (this.config.add) {
      localTime = localTime.add (this.config.add[0], this.config.add[1])
    }

    if (this.config.subtract) {
      localTime = localTime.subtract (this.config.subtract[0], this.config.subtract[1])
    }


    if (this.config.endbleValueOf) {
      localTime = localTime.valueOf();
    }

    
    if (this.config.endbleValueOf) {
      localTime = localTime.valueOf();
    }
    else if (this.config.endbleToDate) {
      localTime = localTime.toDate();
    }
    else if (this.config.endbleFromNow) {
      localTime = localTime.fromNow();
    }
    else {
      localTime = localTime.format(formatString);
    }


    return localTime;
  }



  // Returns the time of the given string
  time(): string { 
    return this.applyMomemntMethods(this.createFormatString("time"));
  }

  // Returns the date of the given string
  date(): string {
    return this.applyMomemntMethods(this.createFormatString("date"));
  }

  // Returns the time & date of the given string
  timeDate(): string {
    const formatString = this.config.timeFirst ? this.createFormatString("time") +  this.config.dateTimeSeparator + this.createFormatString("date") : this.createFormatString("date")+ this.config.dateTimeSeparator + this.createFormatString("time");
    return this.applyMomemntMethods(formatString);
  }
}