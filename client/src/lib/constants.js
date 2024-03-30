export const API_URL = "http://127.0.0.1:8000";
export const cricketurls = {
  cricket_allrounder_odi: "/cricket-allrounder-odi",
  cricket_allrounder_test: "/cricket-allrounder-test",
  cricket_allrounder_t20: "/cricket-allrounder-t20",
};

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
  {
    value: footballurl,
    label: "Football",
  },
  {
    value: "badminton",
    label: "Badminton",
  },
  {
    value: "swimming",
    label: "Swimming",
  },
  {
    value: "chess",
    label: "Chess",
  },
];
