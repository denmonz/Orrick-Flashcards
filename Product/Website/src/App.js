import React, {useCallback, useState, createRef} from 'react'
import {useDropzone} from 'react-dropzone'
import {AppBar, Toolbar, Typography, IconButton, Card, CardContent, Button, Grid, Tabs, Tab, Switch, FormGroup, FormControlLabel } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import GetAppIcon from '@material-ui/icons/GetApp';
import './App.css';
import sampledata from './sampledata';

var mammoth = require("mammoth");

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  title: {
    flexGrow: 1,
  },
  card: {
    width:'80%',
    marginTop: '2%', 
    marginLeft: '5%',
    padding: '5%', 
    flex: 1, 
    flexDirection: 'row'
  }
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


function MyDropzone({upload, setUpload, display, setDisplay}) {
  var text = '';
  var messages = '';

  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.forEach((file) => {
      const reader = new FileReader();

      reader.onabort = () => console.log('file reading was aborted');
      reader.onerror = () => console.log('file reading has failed');
      reader.onload = () => {
      // Do whatever you want with the file contents
        const file_extention = file.name.split('.').pop();
        var arrayBuffer = reader.result;

        if (file_extention === 'txt' || file_extention === 'html') { // for txt or html files
          setUpload(String.fromCharCode.apply(null, new Uint8Array(arrayBuffer)));
          console.log(upload);
        }
        else if (file_extention === 'docx') { // for docx files
          mammoth.extractRawText({arrayBuffer: arrayBuffer})
            .then(function(result) {
                text = result.value; // The generated text
                messages = result.messages; // Any messages, such as warnings during conversion
            })
            .done(function() {
              setUpload(text);
              setDisplay(true);
              console.log(text)
              console.log(messages)
            });
        }
      }
      reader.readAsArrayBuffer(file);
    })
    
  }, [])
  const {getRootProps, getInputProps} = useDropzone({onDrop})

  return (
    <React.Fragment>
      <br/>
      <Typography align='center'>Click or Drag File</Typography>
      <br/>
      <div {...getRootProps()} align='center'>
        <input {...getInputProps()} />
        <IconButton className='download'>
          <GetAppIcon/>
        </IconButton>
      </div>
    </React.Fragment>
  ) 
}

function Flashcard({qna, quiz}) {
  const classes = useStyles();
  const [value, setValue] = useState(0);
  const [key, setKey] = useState(Object.keys(qna));
  const [currval, setCurrval] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  
  if (quiz === true) {
    return(
      <React.Fragment>
      <Tabs value={value} onChange={handleChange} >
        <Tab label="All" index={0}/>
        {key.map((r, index) => 
          <Tab label={r} index={index+1}/>
          )}
      </Tabs>
      {value === 0 ? <AllQuiz qna={qna}/> : null}
      {key.map((r,index) => {
        if (value === index +1) {
          console.log(r)
          return (
            <FilterQuiz filter={r} qna={qna}/>
          )
        }
        else {
          return null
        }
      })}
    </React.Fragment>
    )
  }
  else {
    return(
      <React.Fragment>
        <Tabs value={value} onChange={handleChange} >
          <Tab label="All" index={0}/>
          {key.map((r, index) => 
            <Tab label={r} index={index+1}/>
            )}
        </Tabs>
        {value === 0 ? <AllCard qna={qna}/> : null}
        {key.map((r,index) => {
          if (value === index +1) {
            console.log(r)
            return (
              <FilterCard filter={r} qna={qna}/>
            )
          }
          else {
            return null
          }
        })}
      </React.Fragment>
    )
  }
}

function AllQuiz({qna}) {
  const classes = useStyles();
  const key = Object.keys(qna)
  const [flip, setFlip] = useState(false)

  const handleFlip = () => {
    if (flip === false) {
      setFlip(true)
    }
    else {
      setFlip(false)
    }
  }

  return (
    <React.Fragment>
      <Grid container style={{flexGrow: 1}} spacing={1}>
        {key.map(k =>
          qna[k].map(r => 
            <React.Fragment>
            <Grid item xs={12}>
              <Card className={classes.card} onClick={handleFlip}>
                {flip ? <Typography>{r.answer}</Typography> : <Typography>{r.question}</Typography>}
              </Card>
            </Grid>
          </React.Fragment> 
        ))}
      </Grid>
    </React.Fragment>
  )
}

function FilterQuiz({filter, qna}) {
  const classes = useStyles();
  const [flip, setFlip] = useState(false)

  const handleFlip = () => {
    if (flip === false) {
      setFlip(true)
    }
    else {
      setFlip(false)
    }
  }

  return (
    <React.Fragment>
      <Grid container style={{flexGrow: 1}} spacing={1}>
        {qna[filter].map(r =>
          <React.Fragment>
            <Grid item xs={12}>
              <Card className={classes.card} onClick={handleFlip}>
              {flip ? <Typography>{r.answer}</Typography> : <Typography>{r.question}</Typography>}
              </Card>
            </Grid>
          </React.Fragment> 
        )}
      </Grid>
    </React.Fragment>
  )
}

function AllCard({qna}) {
  const classes = useStyles();
  const key = Object.keys(qna)

  return (
    <React.Fragment>
      <Grid container style={{flexGrow: 1}} spacing={1}>
        {key.map(k =>
          qna[k].map(r => 
            <React.Fragment>
            <Grid item xs={6}>
              <Card className={classes.card}>
                  <Typography>{r.question}</Typography>
              </Card>
            </Grid>
            <Grid item xs={6}>
              <Card className={classes.card}>
                  <Typography>{r.answer}</Typography>
              </Card>
            </Grid>
          </React.Fragment> 
        ))}
      </Grid>
    </React.Fragment>
  )
}

function FilterCard({filter, qna}) {
  const classes = useStyles();

  return (
    <React.Fragment>
      <Grid container style={{flexGrow: 1}} spacing={1}>
        {qna[filter].map(r =>
          <React.Fragment>
            <Grid item xs={6}>
              <Card className={classes.card}>
                  <Typography>{r.question}</Typography>
              </Card>
            </Grid>
            <Grid item xs={6}>
              <Card className={classes.card}>
                  <Typography>{r.answer}</Typography>
              </Card>
            </Grid>
          </React.Fragment> 
        )}
      </Grid>
    </React.Fragment>
  )
}

function App() {
  const [upload, setUpload] = useState('')
  const [qna, setQna] = useState(sampledata)
  const [display, setDisplay] = useState(true)
  const [quiz, setQuiz] = useState(false)

  const handleQuiz = () => {
    if (quiz === true) {
      setQuiz(false)
    }
    else {
      setQuiz(true)
    }
  }

  return (
    <React.Fragment>
      <ButtonAppBar/>
      <MyDropzone upload={upload} setUpload={setUpload} display={display} setDisplay={setDisplay}/>
      <br/>
      <Typography align="center">
        Uploaded text will shown below ↓
      </Typography>
      <br/>
      <Card variant="outlined">
        <CardContent>
          <Typography>
            {upload}
          </Typography>
        </CardContent>
      </Card>
      <Button variant='contained' style={{margin: '1%'}}>Download as PDF</Button>
      <FormGroup style={{margin: '1%'}}>
        <FormControlLabel
          control={
            <Switch checked={quiz} onChange={handleQuiz} lable="Quiz Mode"/>
          }
          label="Quiz Mode"
        />
      </FormGroup>
      {display? <Flashcard qna={qna} quiz={quiz}/>: null}
    </React.Fragment>
  );
}

export default App;
