import React, { Component } from 'react';
import { withStyles } from '@material-ui/core/styles';
import Button from "@material-ui/core/Button";
import store from "../data/store";

const styles = {
  root: {
    position: 'relative',
    width: window.innerWidth,
    height: window.innerHeight,
  }
};

class App extends Component {
  render() {
    const {classes} = this.props;

    return (
      <div className={classes.root}>
        <Button onClick={store.handleChange("TryConnecting")}>Hello</Button>
      </div>
    );
  }
}

export default withStyles(styles)(App);
