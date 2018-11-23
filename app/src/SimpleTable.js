import React, { Component } from "react";
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';

class SimpleTable extends Component {
  render() {
     return (
         <Table>
             <TableHead>
                 <TableRow>
                 {
                     this.props.header.map(column => <TableCell>{column}</TableCell>)
                 }
                 </TableRow>
             </TableHead>
             <TableBody>
             {
                 this.props.rows.map(row =>
                     <TableRow>
                     {
                         row.map(cell =>
                             <TableCell>{cell}</TableCell>
                         )
                     }
                     </TableRow>
                 )
             }
             </TableBody>
         </Table>
     );
  }
}

export default SimpleTable;
