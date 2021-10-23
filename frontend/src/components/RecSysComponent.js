import * as React from 'react';
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
  CardHeader,
} from "@mui/material";
import Paper from '@mui/material/Paper';

const styles = {
  idcell: {
    width: "5%",
  },
  textfield: {
    "margin-right": "2em"
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

class RecSysComponent extends React.Component {
  state = {
    history: [
      {id: "1", text: "Harry Potter", author: "J Rolling", done: false},
      {id: "2", text: "Harry Potter 2", author: "J Rolling", done: false}
    ],
    newTask: "123"
  };

  onTextUpdate = e => {
    this.setState({newTask: e.target.value});
  };

  getRecommendations = () => {
    let {history, newTask} = this.state;
    history.push({text: newTask, done: false});
    this.setState({tasks: history, newTask: ""});
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
    const {history, newTask} = this.state;

    return (
      <div id="main" style={styles.main}>

        <header style={styles.header}>
          <TextField style={styles.textfield}
            label="Add User ID"
            value={newTask}
            onChange={this.onTextUpdate}
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
              {history.length > 0 && (
                <Card
                  variant={"outlined"}
                  style={styles.card}
                >
                  <CardHeader title="Books" avatar={<TimelineIcon/>}/>
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
                              {book.text}
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                </Card>
              )}
            </Grid>
            <Grid item xs={6}>
              {history.length > 0 && (
                <Card variant={"outlined"} style={styles.card}>
                  <CardHeader title="History" avatar={<TimelineIcon/>}/>
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
                              {book.text}
                            </TableCell>
                          </TableRow>
                        ))}
                      </TableBody>
                    </Table>
                  </TableContainer>
                </Card>
              )}
            </Grid>
          </Grid>
        </Container>
      </div>
    );
  }
}

export default RecSysComponent;
