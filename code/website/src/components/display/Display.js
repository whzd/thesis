import React, { Component } from 'react';
import { Card, Collapse } from 'antd';
import './Display.css';

const { Panel } = Collapse;

class Display extends Component {


    render() {
        let displayContent
        let moreInfo
        let definition
        if(this.props.content != null) {
            moreInfo = this.props.content.additionalInfo.map((item, index) => (
                <p><a href={item} key={index}>{item}</a></p>
            ));

            definition = this.props.content.definition.map((item, index) => (
                <div id={index}>
                    <Card title={this.props.content.expression} style={{ width: '90%' }}>
                        <p>{item[0]}</p>
                    </Card>
                    <br />
                </div>
            ));

            displayContent =
                <div>
                        {definition}
                    <Collapse accordion style={{ width: '90%' }}>
                        <Panel header="Fontes" key="1">
                            <p><a href={this.props.content.source}>{this.props.content.source}</a></p>
                        </Panel>
                        <Panel header="Informação Adicional" key="2">
                                {moreInfo}
                        </Panel>
                    </Collapse>
                </div>
        }else{
            displayContent = ""
        }

        return (
            <div className="Display">
                    { displayContent }
            </div>
        )
    }
}

export default Display;
