import React, { Component } from 'react';
import './App.css';
import Form from 'react-bootstrap/Form';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Button from 'react-bootstrap/Button';
import "bootstrap/dist/css/bootstrap.css";
import API from "./API";

class App extends Component {

  constructor(props) {
    super(props);

    this.state = {
      isLoading: false,
      formData: {
        loss: '',
        optimizer: '',
        epochs: 1,
        batch_size: 1,
        dropout: 0
      },
      result: ""
    };
  }

  handleChange = (event) => {
    const value = event.target.value;
    const name = event.target.name;
    var formData = this.state.formData;
    formData[name] = value;
    this.setState({
      formData
    });
  }

  handlePredictClick = async (event) => {
    const formData = this.state.formData;
    console.log(formData);
    this.setState({ isLoading: true });
    let returned = await API.get("/model", { params: { loss: this.state.formData.loss, optimizer: this.state.formData.optimizer, epochs: this.state.formData.epochs, batch_size: this.state.formData.batch_size, dropout: this.state.formData.dropout  } });
    console.log(returned);
    this.setState({ isLoading: false, result: returned.data.result });
  }

  handleCancelClick = (event) => {
    this.setState({ result: "" });
  }

  render() {
    const isLoading = this.state.isLoading;
    const formData = this.state.formData;
    const result = this.state.result;

    return (
      <Container>
        <div>
          <h1 className="title">Machine Learning Cloud Computing Predictor</h1>
        </div>
        <div className="content">
          <Form>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>Loss</Form.Label>
                <Form.Control 
                  type="text" 
                  placeholder="loss" 
                  name="loss"
                  value={formData.loss}
                  onChange={this.handleChange} />
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Optimizer</Form.Label>
                <Form.Control 
                  type="text" 
                  placeholder="Optimizer" 
                  name="optimizer"
                  value={formData.optimizer}
                  onChange={this.handleChange} />
              </Form.Group>
            </Form.Row>
            <Form.Row>
              <Form.Group as={Col}>
                <Form.Label>Epochs</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.epochs}
                  name="epochs"
                  onChange={this.handleChange}>
                  <option>1</option>
                  <option>4</option>
                  <option>8</option>
                  <option>16</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Batch Size</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.batch_size}
                  name="batch_size"
                  onChange={this.handleChange}>
                  <option>1</option>
                  <option>5</option>
                  <option>10</option>
                  <option>15</option>
                </Form.Control>
              </Form.Group>
              <Form.Group as={Col}>
                <Form.Label>Dropout</Form.Label>
                <Form.Control 
                  as="select"
                  value={formData.dropout}
                  name="dropout"
                  onChange={this.handleChange}>
                  <option>0.0</option>
                  <option>0.1</option>
                  <option>0.2</option>
                  <option>0.3</option>
                </Form.Control>
              </Form.Group>
            </Form.Row>
            <Row>
              <Col>
                <Button
                  block
                  variant="success"
                  disabled={isLoading}
                  onClick={!isLoading ? this.handlePredictClick : null}>
                  { isLoading ? 'Making prediction' : 'Predict' }
                </Button>
              </Col>
              <Col>
                <Button
                  block
                  variant="danger"
                  disabled={isLoading}
                  onClick={this.handleCancelClick}>
                  Reset prediction
                </Button>
              </Col>
            </Row>
          </Form>
          {result === "" ? null :
            (<Row>
              <Col className="result-container">
                <h5 id="result">{result}</h5>
              </Col>
            </Row>)
          }
        </div>
      </Container>
    );
  }
}

export default App;