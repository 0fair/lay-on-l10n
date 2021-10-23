import React from "react";
import { render } from "react-dom";
import TodoComponent from "./components/TodoComponent";
import { MuiThemeProvider, createMuiTheme } from "material-ui/styles";
import blue from "material-ui/colors/blue";

const theme = createMuiTheme({
  palette: {
    primary: blue,
    type: "light" // Switching the dark mode on is a single property value change.
  }
});

const App = () => (
  <MuiThemeProvider theme={theme}>
    <TodoComponent />
  </MuiThemeProvider>
);

render(<App />, document.getElementById("root"));
