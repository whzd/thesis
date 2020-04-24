import React, { Component } from 'react';

class Display extends Component {
    render() {
        const { string } = this.props
        const stringList = string.map(str => {
            return (
                <p> { str } </p>
            )
        })

        return (
            <div className="Display">
            Display block
            { stringList }
            </div>
        )
    }
}

export default Display;
