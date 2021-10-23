import React from "react";
import { render } from "react-dom";

import RecSysComponent from "./components/RecSysComponent";
import CssBaseline from '@mui/material/CssBaseline';
import {ThemeProvider} from "@mui/material/styles";
import {AppBar, Avatar, Box, Button, createTheme, MenuItem, Toolbar, Typography} from "@mui/material";
import {blue, blueGrey} from "@mui/material/colors";
import lion from "./img/lion.png"
import IconButton from "@mui/material/IconButton";

const theme = createTheme({
  palette: {
    primary: blue,
    secondary: blueGrey,
    type: "light" // Switching the dark mode on is a single property value change.
  }
});

const App = () => (
  <ThemeProvider theme={theme}>
    <CssBaseline />
    <Box sx={{flexGrow: 0.5}}>
      <AppBar position="static">
        <Toolbar>
          <Avatar alt="Lay-On-L10n" src={lion} style={{"margin-right": "0.5em"}}/>
          <Typography variant="h7" component="div" sx={{flexGrow: 0.5}}>
            Lay-On-L10n
          </Typography>
        </Toolbar>
      </AppBar>
    </Box>
    <br/>
    <RecSysComponent />
  </ThemeProvider>
);

render(<App />, document.getElementById("root"));
