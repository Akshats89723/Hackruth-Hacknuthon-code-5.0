// src/App.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [questions, setQuestions] = useState([]);
  const [currentQuestion, setCurrentQuestion] = useState('');
  const [answer, setAnswer] = useState('');

  useEffect(() => {
    axios.get('/questions')
      .then(response => {
        setQuestions(response.data.questions);
      });
  }, []);

  const handleQuestionClick = (question) => {
    setCurrentQuestion(question);
  };

  const handleAnswerChange = (e) => {
    setAnswer(e.target.value);
  };

  const submitAnswer = () => {
    axios.post('/answer', { question: currentQuestion })
      .then(response => {
        setCurrentQuestion('');
        setAnswer('');
      });
  };

  return (
    <div>
      <h1>Virtual HR Manager</h1>
      {currentQuestion ? (
        <div>
          <h2>{currentQuestion}</h2>
          <input type="text" value={answer} onChange={handleAnswerChange} />
          <button onClick={submitAnswer}>Submit Answer</button>
        </div>
      ) : (
        <ul>
          {questions.map(question => (
            <li key={question} onClick={() => handleQuestionClick(question)}>
              {question}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}

export default App;
