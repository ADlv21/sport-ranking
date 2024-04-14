export const APP_NAME = "SportsBug";

export const API_URL = "http://127.0.0.1:8000";

export const cricketurls = {
  cricket_allrounder_odi: "/cricket-allrounder-odi",
  cricket_allrounder_test: "/cricket-allrounder-test",
  cricket_allrounder_t20: "/cricket-allrounder-t20",
  cricket_bowl_odi: "/cricket-bowl-odi",
  cricket_bowl_test: "/cricket-bowl-test",
  cricket_bowl_t20: "/cricket-bowl-t20",
  cricket_bat_odi: "/cricket-bat-odi",
  cricket_bat_test: "/cricket-bat-test",
  cricket_bat_t20: "/cricket-bat-t20",
};

export const chessurl = "/chess";

export const footballurl = "/football";

export const sports = [
  {
    value: cricketurls.cricket_allrounder_odi,
    label: "Cricket All Rounder ODI",
  },
  {
    value: cricketurls.cricket_allrounder_test,
    label: "Cricket All Rounder Test",
  },
  {
    value: cricketurls.cricket_allrounder_t20,
    label: "Cricket All Rounder T20",
  },
  { value: cricketurls.cricket_bowl_odi, label: "Cricket Bowler ODI" },
  { value: cricketurls.cricket_bowl_test, label: "Cricket Bowler Test" },
  { value: cricketurls.cricket_bowl_t20, label: "Cricket Bowler T20" },
  { value: cricketurls.cricket_bat_odi, label: "Cricket Batsman ODI" },
  { value: cricketurls.cricket_bat_test, label: "Cricket Batsman Test" },
  { value: cricketurls.cricket_bat_t20, label: "Cricket Batsman T20" },
  {
    value: footballurl,
    label: "Football",
  },
  {
    value: chessurl,
    label: "Chess",
  },
  {
    value: "badminton",
    label: "Badminton",
  },
  {
    value: "swimming",
    label: "Swimming",
  },
];
