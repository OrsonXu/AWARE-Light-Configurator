import React from "react";
import Box from "@mui/material/Box";
import Grid from "@mui/material/Unstable_Grid2";
import { Button, Link, ThemeProvider } from "@mui/material";
import { useNavigate } from "react-router-dom";
import ScheduleComponent from "../components/ScheduleComponent/ScheduleComponent";
import "./StudyQuestions.css";
import customisedTheme from "../functions/theme";

export default function ScheduleConfiguration() {
  const navigateTo = useNavigate();
  return (
    <ThemeProvider theme={customisedTheme}>
      <div className="study_question_vertical_layout">
        <ScheduleComponent scheduleNumber={1} />
        <ScheduleComponent scheduleNumber={2} />

        <Box sx={{ width: "100%" }} mt={5} marginBottom={5}>
          <Grid
            container
            rowSpacing={1}
            columnSpacing={{ xs: 1, sm: 2, md: 23 }}
          >
            <Grid xs={12}>
              <Button
                color="main"
                variant="contained"
                onClick={() => {
                  // todo
                  alert("add new question has not implemented");
                }}
              >
                ADD A NEW SCHEDULE
              </Button>
            </Grid>
            <Grid xs={6}>
              <Button
                color="main"
                variant="contained"
                onClick={() => {
                  navigateTo("/study/study_information");
                }}
              >
                BACK
              </Button>
            </Grid>
            <Grid xs />
            <Grid xs="auto">
              <Button
                color="main"
                variant="contained"
                onClick={() => {
                  navigateTo("/study/schedule_configuration");
                }}
              >
                NEXT STEP: SENSOR DATA
              </Button>
            </Grid>
          </Grid>
        </Box>
      </div>
    </ThemeProvider>
  );
}
