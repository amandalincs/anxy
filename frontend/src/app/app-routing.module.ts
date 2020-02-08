import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { JournalComponent } from './components/journal/journal.component';
import { ReflectComponent } from './components/reflect/reflect.component';
import { InspireComponent } from './components/inspire/inspire.component';

const routes: Routes = [
  { path: 'journal', component: JournalComponent },
  { path: 'reflect', component: ReflectComponent },
  { path: 'inspire', component: InspireComponent },
  { path: '**', redirectTo: 'journal', pathMatch: 'full' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
