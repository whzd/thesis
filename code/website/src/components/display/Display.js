import React, { Component } from 'react';
import { Card, Collapse } from 'antd';

    const { Panel } = Collapse;

class Display extends Component {


    render() {
        let definition
        if(this.props.content != null) {
            definition = <div>
                <Card title={this.props.content.expression} style={{ width: '90%' }}>
                <p>{this.props.content.definition}</p>
                </Card>
                <br />
                <br />
                <Collapse accordion style={{ width: '90%' }}>
                <Panel header="Fontes" key="1">
                <p><a href={this.props.content.sources[0]}>{this.props.content.sources[0]}</a></p>
                <p><a href={this.props.content.sources[1]}>{this.props.content.sources[1]}</a></p>
                <p><a href={this.props.content.sources[2]}>{this.props.content.sources[2]}</a></p>
                </Panel>
                </Collapse>
                </div>
        }else{
            definition = ""
        }

        return (
            <div className="Display">
            { definition }
            </div>
        )
    }
}

export default Display;
