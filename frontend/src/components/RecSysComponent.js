import * as React from 'react';
import axios from 'axios';

import Container from '@mui/material/Container';
import TextField from "@mui/material/TextField";
import Button from '@mui/material/Button';
import Card from "@mui/material/Card";
import TimelineIcon from '@mui/icons-material/Timeline';
import {
  Grid,
  Table,
  TableRow,
  TableContainer,
  TableCell,
  TableBody,
  TableHead,
  CardHeader, Alert,
} from "@mui/material";
import Paper from '@mui/material/Paper';
import {Book, BookmarkBorder} from "@mui/icons-material";

const styles = {
  idcell: {
    width: "5%",
  },
  textfield: {
    marginRight: "2em"
  },
  authorcell: {
    width: "20%"
  },
  titlecell: {
    width: "75%"
  },
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

class RecSysComponent extends React.Component {
  state = {
    alertMessage: "",
    history: [],
    recommendations: [],
    newTask: ""
  };

  onTextUpdate = e => {
    this.setState({newTask: e.target.value});
  };
  onEnterUpdate = e => {
    if (e.keyCode === 13) {
      this.setState({newTask: e.target.value});
      this.getRecommendations()
    }
  };

  setEmptyState() {
    this.setState({
      history: [],
      recommendations: [],
      newTask: ""
    })
  }

  getRecommendations = () => {
    let {newTask} = this.state;
    if (newTask === "") {
      this.setEmptyState();
      return;
    }

    if (isNaN(newTask)) {
      this.setState({alertMessage: "Book ID have to be a number!"})
      return;
    } else {
      this.setState({alertMessage: ""})
    }

    axios
      .get('http://localhost:8080/api/v1/recsys/recsys/' + newTask)
      .then(res => {
        const result = res.data;
        console.log(result)
        if (result.history !== undefined) {
          this.setState({
            history: result.history,
            recommendations: result.recommendations
          });
        }
      })

  };

  deleteTask = task => {
    let {history} = this.state;
    history.splice(history.indexOf(task), 1);
    this.setState({tasks: history, newTask: ""});
  };

  toggle = task => {
    let {history} = this.state;
    history[history.indexOf(task)].done = !history[history.indexOf(task)].done;
    this.setState({tasks: history, newTask: ""});
  };

  render() {
    const {recommendations, history, newTask} = this.state;

    return (
      <div id="main" style={styles.main}>
        {this.state.alertMessage !== "" &&
        <Alert variant="outlined" severity="error">
          {this.state.alertMessage}
        </Alert>
        }
        <br />
        <header style={styles.header}>
          <TextField style={styles.textfield}
                     label="Add User ID"
                     value={newTask}
                     inputProps={{inputMode: 'numeric', pattern: '[0-9]+'}}
                     onChange={this.onTextUpdate}
                     onKeyUp={this.onEnterUpdate}
          />
          <Button
            variant="contained"
            disabled={!newTask}
            onClick={this.getRecommendations}
          >
            Recommend
          </Button>
        </header>
        <Container maxWidth="xl">
          <Grid container spacing={2}>
            <Grid item xs={6}>

              <Card
                variant={"outlined"}
                style={styles.card}
              >
                <CardHeader title="Books Recommendations" avatar={<BookmarkBorder/>}/>
                <TableContainer component={Paper}>
                  <Table sx={{minWidth: 200}} aria-label={"simple tabke"}>
                    <TableHead>
                      <TableRow>
                        <TableCell style={styles.idcell}>Book ID</TableCell>
                        <TableCell style={styles.authorcell}>Author</TableCell>
                        <TableCell style={styles.titlecell}>Title</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {recommendations.map((book, index) => (
                        <TableRow selected={true} key={index}>
                          <TableCell style={styles.idcell}>
                            {book.id}
                          </TableCell>
                          <TableCell style={styles.authorcell}>
                            {book.author}
                          </TableCell>
                          <TableCell style={styles.titlecell}>
                            {book.title}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </TableContainer>
              </Card>
            </Grid>
            <Grid item xs={6}>
              <Card variant={"outlined"} style={styles.card}>
                <CardHeader title="User History" avatar={<TimelineIcon/>}/>
                <TableContainer component={Paper}>
                  <Table sx={{minWidth: 200}} aria-label={"simple tabke"}>
                    <TableHead>
                      <TableRow>
                        <TableCell style={styles.idcell}>Book ID</TableCell>
                        <TableCell style={styles.authorcell}>Author</TableCell>
                        <TableCell style={styles.titlecell}>Title</TableCell>
                      </TableRow>
                    </TableHead>
                    <TableBody>
                      {history.map((book, index) => (
                        <TableRow selected={true} key={index}>
                          <TableCell style={styles.idcell}>
                            {book.id}
                          </TableCell>
                          <TableCell style={styles.authorcell}>
                            {book.author}
                          </TableCell>
                          <TableCell style={styles.titlecell}>
                            {book.title}
                          </TableCell>
                        </TableRow>
                      ))}
                    </TableBody>
                  </Table>
                </TableContainer>
              </Card>
            </Grid>
          </Grid>
        </Container>
      </div>
    );
  }
}

export default RecSysComponent;
