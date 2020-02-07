import React, {useCallback} from 'react'
import {useDropzone} from 'react-dropzone'
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import GetAppIcon from '@material-ui/icons/GetApp';
import { IconButton } from '@material-ui/core';
import './App.css';
import firebase from 'firebase/app';
import 'firebase/database';

const firebaseConfig = {
  apiKey: "AIzaSyBRgb3Ed9B9bg_dXi_VtMpoT3Ezr_MK83A",
  authDomain: "orrick-flashcards.firebaseapp.com",
  databaseURL: "https://orrick-flashcards.firebaseio.com",
  projectId: "orrick-flashcards",
  storageBucket: "orrick-flashcards.appspot.com",
  messagingSenderId: "744134644092",
  appId: "1:744134644092:web:a557f652b0d0ca6d6594f9"
};

firebase.initializeApp(firebaseConfig);

const db = firebase.database().ref();

var mammoth = require("mammoth");

const useStyles = makeStyles(theme => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
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

function MyDropzone() {
  var upload = '';
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
          upload = String.fromCharCode.apply(null, new Uint8Array(arrayBuffer));
          console.log(upload);
        }
        else if (file_extention === 'docx') { // for docx files
          mammoth.extractRawText({arrayBuffer: arrayBuffer})
            .then(function(result) {
                text = result.value; // The generated text
                messages = result.messages; // Any messages, such as warnings during conversion
            })
            .done(function() {
              upload = text;
              console.log(upload)
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

function App() {
  return (
    <React.Fragment>
      <ButtonAppBar/>
      <MyDropzone/>
    </React.Fragment>
  );
}

export default App;