import React from "react";
import TextField from "material-ui/TextField";
import Button from "material-ui/Button";
import IconButton from "material-ui/IconButton";
import Card from "material-ui/Card";
import Divider from "material-ui/Divider";
import Switch from "material-ui/Switch";
import DeleteIcon from "material-ui-icons/Delete";
import Tooltip from "material-ui/Tooltip";
import {FormGroup, FormControlLabel} from "material-ui/Form";
import {Grid} from "material-ui";

const styles = {
  done: {
    textDecoration: "line-through",
    opacity: ".5",
    display: "flex",
    width: "100%"
  },
  header: {
    justifyContent: "center",
    display: "flex",
    flexDirection: "row",
    alignItems: "center"
  },
  main: {
    width: "100%",
    maxWidth: "400px",
    margin: "20px auto"
  },
  card: {
    padding: "20px",
    margin: "20px 0"
  },
  todo: {
    position: "relative",
    display: "flex",
    flexFow: "row",
    alignContent: "space-between"
  },
  label: {
    display: "flex",
    width: "100%"
  },
  divider: {
    position: "absolute",
    width: "100%",
    top: 0
  }
};

class TodoComponent extends React.Component {
  state = {
    tasks: [],
    newTask: ""
  };

  onTextUpdate = e => {
    this.setState({newTask: e.target.value});
  };

  getRecommendations = () => {
    let {tasks, newTask} = this.state;
    tasks.push({text: newTask, done: false});
    this.setState({tasks: tasks, newTask: ""});
  };

  deleteTask = task => {
    let {tasks} = this.state;
    tasks.splice(tasks.indexOf(task), 1);
    this.setState({tasks: tasks, newTask: ""});
  };

  toggle = task => {
    let {tasks} = this.state;
    tasks[tasks.indexOf(task)].done = !tasks[tasks.indexOf(task)].done;
    this.setState({tasks: tasks, newTask: ""});
  };

  render() {
    const {tasks, newTask} = this.state;

    return (
      <div id="main" style={styles.main}>
        <header style={styles.header}>
          <TextField
            label="Add User ID"
            value={newTask}
            onChange={this.onTextUpdate}
          />
          <Button
            variant="raised"
            color="primary"
            disabled={!newTask}
            onClick={this.getRecommendations}
          >
            Add
          </Button>
        </header>
        <Container maxWidth="sm">
          <Grid container spacing={2}>
            <Grid item xs={6}>
              {tasks.length > 0 && (
                <Card style={styles.card}>
                  <FormGroup>
                    {tasks.map((task, index) => (
                      <div key={index} style={styles.todo}>
                        {index > 0 ? <Divider style={styles.divider}/> : ""}
                        <FormControlLabel
                          control={
                            <Switch
                              color="primary"
                              checked={!task.done}
                              onChange={() => this.toggle(task)}
                            />
                          }
                          label={task.text}
                          style={task.done ? styles.done : styles.label}
                        />
                        <Tooltip title="Delete task" placement="top">
                          <IconButton
                            aria-label="delete"
                            onClick={() => this.deleteTask(task)}
                          >
                            <DeleteIcon/>
                          </IconButton>
                        </Tooltip>
                      </div>
                    ))}
                  </FormGroup>
                </Card>
              )}
            </Grid>
            <Grid item xs={6}>
              {tasks.length > 0 && (
                <Card style={styles.card}>
                  <FormGroup>
                    {tasks.map((task, index) => (
                      <div key={index} style={styles.todo}>
                        {index > 0 ? <Divider style={styles.divider}/> : ""}
                        <FormControlLabel
                          control={
                            <Switch
                              color="primary"
                              checked={!task.done}
                              onChange={() => this.toggle(task)}
                            />
                          }
                          label={task.text}
                          style={task.done ? styles.done : styles.label}
                        />
                        <Tooltip title="Delete task" placement="top">
                          <IconButton
                            aria-label="delete"
                            onClick={() => this.deleteTask(task)}
                          >
                            <DeleteIcon/>
                          </IconButton>
                        </Tooltip>
                      </div>
                    ))}
                  </FormGroup>
                </Card>
              )}
            </Grid>
          </Grid>
        </Container>
      </div>
    );
  }
}

export default TodoComponent;
