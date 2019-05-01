import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import axios from 'axios';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';

const requests = axios.create({
  headers: {
    'X-CSRFToken': csrf_token,
    'Content-Type': 'application/json',
  },
});

ReactDOM.render(<p></p>, document.getElementById('react-container'));
