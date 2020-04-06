import React, {useCallback, useState, useEffect} from 'react'
import Generator from './Generator';
import './App.css';
import {AppBar, Toolbar, Typography, TextField, Button, Grid} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  title: {
    flexGrow: 1,
  },
}));

function ButtonAppBar() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
            Flashcard Generator
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
}

function LoginPage({login, setLogin}) {
  const [wrong, setWrong] = useState(false)
  const [pass, setPass] = useState('')

  const handleChange = (e) => {
    setPass(e.target.value)
  } 

  const handleClick = () => {
    if (pass === 'orrick') {
      setWrong(false)
      setLogin(true)
    }
    else {
      setWrong(true)
    }
  }

  return (
    <React.Fragment>
      <Grid
        container
        direction="column"
        justify="center"
        alignItems="center"
        style={{marginTop: '20%'}}
      >
        <Grid item>
          <TextField
            id="outlined"
            variant="outlined"
            label="Password"
            onChange={(e) => handleChange(e)}
          />
        </Grid>
        {wrong ? <Typography color="error">Wrong Password</Typography>: null}
        <Grid item>
          <Button variant="contained" onClick={handleClick} style={{marginTop: '10%'}}>Login</Button>
        </Grid>
      </Grid>
    </React.Fragment>
  )
}

function App() {
  const [login, setLogin] = useState(false)

  return (
    <React.Fragment>
    <ButtonAppBar/>
    {login? <Generator/> : <LoginPage login={login} setLogin={setLogin}/>}
    </React.Fragment>
  );
}

export default App;
