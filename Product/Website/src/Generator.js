import React, {useCallback, useState, useEffect} from 'react'
import {useDropzone} from 'react-dropzone'
import {AppBar, Toolbar, TextField, Typography, IconButton, Card, Container, Button, Grid, Tabs, Tab, Switch, FormGroup, FormControlLabel } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import GetAppIcon from '@material-ui/icons/GetApp';
import './Generator.css';
import sampledata from './sampledata';
import axios from 'axios';

var mammoth = require("mammoth");

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  title: {
    flexGrow: 1,
  },
  card: {
    flex: 1,
    width:'80%',
    height: '15vw',
    marginTop: '2%', 
    marginLeft: '5%',
    padding: '5%', 
  },
  cardtext: {
    fontSize: 30,
    marginLeft: '2%',
    marginRight: '2%'
  },
  textcontainer: {
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    height: '100%',
    margin: 0,
  },
  background: {
    backgroundColor: 'grey',
    flex: 1
  }
}));

function MyDropzone({upload, setUpload, display, setDisplay, qna, setQna}) {
  var text = '';
  var messages = '';

  const fetchFlask = (text) => {
    console.log("fetching python localhost");
    // fetch('http://127.0.0.1:5000/q').then(response => response.json().then(data => setQna(data)))
    // axios.post('http://127.0.0.1:5000/q', {data: text}).then(response => response.json().then(output => setQna(output)))
    axios.post('http://127.0.0.1:5000/q', {data: text}).then(response => setQna(response.data))
    // useEffect(() => {
    //   fetch('/a').then(response => response.json().then(data => {console.log(data);}))
    // },[])
    // fetch('/a', {
    //   method: 'GET',
    //   mode:'no-cors',
    //   dataType: 'json'
    // })
    //   .then(r => r.json())
    //   .then(r => {
    //     console.log(r);
    //     setQna(r);
    //   })
    //   .catch(err => console.log(err))
  }

  const onDrop = useCallback((acceptedFiles) => {
    acceptedFiles.forEach((file) => {
      const reader = new FileReader();
      
      reader.onabort = () => console.log('file reading was aborted');
      reader.onerror = () => console.log('file reading has failed');
      reader.onload = () => {
      // Do whatever you want with the file contents
        const file_extention = file.name.split('.').pop();
        var arrayBuffer = reader.result;

        // if (file_extention === 'txt' || file_extention === 'html') { // for txt or html files
        //   // setUpload(String.fromCharCode.apply(null, new Uint8Array(arrayBuffer)));
        //   console.log(upload);
        //   setUpload(text);
        //   setDisplay(true);
        // }
        if (file_extention === 'docx') { // for docx files
          mammoth.extractRawText({arrayBuffer: arrayBuffer})
            .then(function(result) {
                text = result.value; // The generated text
                messages = result.messages; // Any messages, such as warnings during conversion
            })
            // .then(function() {
            //   setUpload(text);
            //   console.log(text)
            // })
            .then(function() {
              fetchFlask(text);
            })
            .done(function() {
              setDisplay(true);
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

function Flashcard({ qna, quiz, heading }) {
  const classes = useStyles();
  const [value, setValue] = useState(0);
  
  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
  if (heading === undefined) {
    return(null)
  }
  else {
    if (quiz === true) {
      return(
        <React.Fragment>
        <Tabs value={value} onChange={handleChange} >
          <Tab label="All" index={0}/>
          {heading.map((r, index) => 
            <Tab label={r} index={index+1}/>
            )}
        </Tabs>
        {value === 0 ? <AllQuiz qna={qna}/> : null}
        {heading.map((r,index) => {
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
            {heading.map((r, index) => 
              <Tab label={r} index={index+1}/>
              )}
          </Tabs>
          {value === 0 ? <AllCard qna={qna}/> : null}
          {heading.map((r,index) => {
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
}

function AllQuiz({qna}) {
  const classes = useStyles();
  const key = Object.keys(qna)
  
  var total_len = 0;
  for (var i=0; i < key.length; i++) {
    total_len += qna[key[i]].length
  }

  const [flip, setFlip] = useState(Array.apply(null, Array(key.length)).map(function (x) { return Array.apply(null, Array(total_len)).map(function (x) {return false}); }))

  const handleFlip = (index, key) => {
    if (flip[key][index] === false) {
      let old = flip.slice()
      old[key][index] = true
      setFlip(old)
    }
    else {
      let old = flip.slice()
      old[key][index] = false
      setFlip(old)
    }
  }

  return (
    <React.Fragment>
      <Grid container style={{flexGrow: 1}} spacing={1}>
        {key.map((k,j) =>
          qna[k].map((r,i) => 
            <React.Fragment>
            <Grid item xs={12}>
              <Card className={classes.card} onClick={() => handleFlip(i,j)}>
                <div className={classes.textcontainer}>
                  {flip[j][i] ? <Typography className={classes.cardtext}>Answer: {r.answer}</Typography> : <Typography className={classes.cardtext}>Question: {r.question}</Typography>}
                </div>
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

  const [flip, setFlip] = useState(Array.apply(null, Array(qna[filter].length)).map(function (x) { return false }))

  const handleFlip = (index) => {
    if (flip[index] === false) {
      let old = flip.slice()
      old[index] = true
      setFlip(old)
    }
    else {
      let old = flip.slice()
      old[index] = false
      setFlip(old)
    }
  }

  return (
    <React.Fragment>
      <Grid container style={{flexGrow: 1}} spacing={1}>
        {qna[filter].map((r, i) =>
          <React.Fragment>
            <Grid item xs={12}>
              <Card className={classes.card} onClick={() => handleFlip(i)}>
                <div className={classes.textcontainer}>
                  {flip[i] ? <Typography className={classes.cardtext}>Answer: {r.answer}</Typography> : <Typography className={classes.cardtext}>Question: {r.question}</Typography>}
                </div>
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
                <div className={classes.textcontainer}>
                  <Typography className={classes.cardtext}>{r.question}</Typography>
                </div>
              </Card>
            </Grid>
            <Grid item xs={6}>
              <Card className={classes.card}>
                <div className={classes.textcontainer}>
                  <Typography className={classes.cardtext}>{r.answer}</Typography>
                </div>
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
                <div className={classes.textcontainer}>
                  <Typography className={classes.cardtext}>{r.question}</Typography>
                </div>
              </Card>
            </Grid>
            <Grid item xs={6}>
              <Card className={classes.card}>
                <div className={classes.textcontainer}>
                  <Typography className={classes.cardtext}>{r.answer}</Typography>
                </div>
              </Card>
            </Grid>
          </React.Fragment> 
        )}
      </Grid>
    </React.Fragment>
  )
}

function AddFlashcard({add, setAdd, qna, setQna, heading, setHeading}) {
  const [newq, setNewq] = useState('')
  const [newa, setNewa] = useState('')
  const [noinput, setNoinput] = useState(false)
  let temp = qna

  const handleQuestion = (e) => {
    setNewq(e.target.value)
  } 

  const handleAnswer = (e) => {
    setNewa(e.target.value)
  } 

  const handleClick = () => {
    if (newq != '' && newa != '') {
      setAdd(false)
      setNoinput(false)
      if (temp['Added'] === undefined) {
        temp['Added'] = [{'question': newq, 'answer': newa}]
        setQna(temp)
        setHeading(Object.keys(temp))
        console.log(temp)
      }
      else {
        temp['Added'].push({'question': newq, 'answer': newa})
        setQna(temp)
        console.log(temp)
      }
    }
    else {
      setNoinput(true)
    }
  }

  return (
    <React.Fragment>
      <Grid
        container
        direction="column"
        justify="center"
        alignItems="left"
        style={{marginLeft: '10%', marginTop: '2%', marginBottom: '2%'}}
      >
        <Grid item style={{marginBottom: '1%'}}>
          <TextField
            variant="filled"
            label="New Question"
            onChange={(e) => handleQuestion(e)}
          />
        </Grid>
        <Grid item style={{marginBottom: '1%'}}>
          <TextField
            variant="filled"
            label="New Answer"
            onChange={(e) => handleAnswer(e)}
          />
        </Grid>
        {noinput ? <Typography color="error">Enter Question and Answer</Typography>: null}
        <Grid item>
          <Button variant="contained" color="primary" onClick={handleClick}>Add</Button>
        </Grid>
      </Grid>
    </React.Fragment>
  )
}

function Generator() {
  const [upload, setUpload] = useState('')
  const [qna, setQna] = useState({})
  const [display, setDisplay] = useState(false)
  const [quiz, setQuiz] = useState(false)
  const [add, setAdd] = useState(false)
  const [heading, setHeading] = useState([])

  useEffect(() => {
    setHeading(Object.keys(qna));
  }, [qna, display]);

  // useEffect(() => {
  //   fetch('http://127.0.0.1:5000/q',{mode:'no-cors',dataType:'json'}).then(response => response.json().then(data => {console.log(data);}))
  // },[])
  const handleQuiz = () => {
    if (quiz === true) {
      setQuiz(false)
    }
    else {
      setQuiz(true)
    }
  }

  const handleNew = () => {
    setDisplay(false)
  }

  const handleAdd = () => {
    setAdd(true)
  }

  return (
    <React.Fragment>
      {display? null : <MyDropzone upload={upload} setUpload={setUpload} display={display} setDisplay={setDisplay} qna={qna} setQna={setQna}/>}
      <br/>
      {display? 
      <React.Fragment>
        <Button variant='contained' style={{margin: '1%'}} onClick={() => window.print()}>Download as PDF</Button>
        <Button variant='contained' color='primary' onClick={handleAdd} style={{margin: '1%'}}>Add New Flashcard</Button>
        <Button variant='contained' color='secondary' onClick={handleNew} style={{margin: '1%'}}>Upload New Document</Button>
        {add ? <AddFlashcard add={add} setAdd={setAdd} qna={qna} setQna={setQna} heading={heading} setHeading={setHeading} /> : null }
        <FormGroup style={{margin: '1%'}}>
          <FormControlLabel
            control={
              <Switch checked={quiz} onChange={handleQuiz} lable="Quiz Mode"/>
            }
            label="Quiz Mode"
          />
        </FormGroup>
        <Flashcard qna={qna} quiz={quiz} heading={heading}/> 
      </React.Fragment>: null}
    </React.Fragment>
  );
}

export default Generator;
