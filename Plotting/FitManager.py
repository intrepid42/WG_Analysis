import ROOT

class FitManager : 

    def __init__(self, typename, norders, sampname, hist, plot_var, ieta, xvar, label, useRooFit) :

        self.defs = {}

        self.func_name = typename
        self.func_norders = norders

        self.sample_name = sampname
        self.plot_var = plot_var

        self.ieta = ieta

        self.hist = hist
        self.xvar = xvar

        self.label = label

        self.func = None
        self.func_pdf = None

        self.useRooFit = useRooFit

        self.hist.SetLineColor( ROOT.kBlack )
        self.hist.SetMarkerColor( ROOT.kBlack )
        self.hist.SetMarkerStyle( 20 )
        self.hist.SetMarkerSize( 1.0 )

        self.datahist = ROOT.RooDataHist( 'datahist_%s' %self.label, 'data', ROOT.RooArgList(self.xvar), self.hist )
        ROOT.SetOwnership( self.datahist, False )
        
        self.get_defaults( sampname, plot_var, ieta )

    def Integral( self ) :

        return self.hist.Integral( self.hist.FindBin( self.xvar.getMin() ), self.hist.FindBin( self.xvar.getMax() ) )

    def set_vals(self, name, order, vals ) :

        self.defs.setdefault( name, {} )
        self.defs[name][order] = vals

    def get_vals( self, name, order ) :

        return self.defs[name][order]

    def add_vars( self, arg_list) :

        if self.func_name == 'dijet' : 
            for i in range( 1, self.func_norders+1 ) :
                this_def = self.get_vals( self.func_name, i )
                var = ROOT.RooRealVar( 'order%d' %i, 'order%d' %i, this_def[0], this_def[1], this_def[2] )
                ROOT.SetOwnership(var, False)
                var.SetName( '%s_order%d' %( self.func_name, i ) )
                arg_list.add( var  ) 

        if self.func_name == 'atlas' : 
            def_num_power = self.get_vals( self.func_name+'_num_power', 1 )
            def_den_power = self.get_vals( self.func_name+'_den_power', 1 )

            var_num_power = ROOT.RooRealVar( 'num_power', 'num_power', def_num_power[0], def_num_power[1], def_num_power[2] )
            var_den_power = ROOT.RooRealVar( 'den_power', 'den_power', def_den_power[0], def_den_power[1], def_den_power[2] )
            ROOT.SetOwnership(var_num_power, False)
            ROOT.SetOwnership(var_den_power, False)
            arg_list.add( var_num_power )
            arg_list.add( var_den_power )
            for i in range( 1, self.func_norders+1 ) :
                def_den_logcoef = self.get_vals( self.func_name+'_den_logcoef', i )
                var_den_locoef  = ROOT.RooRealVar( 'den_logcoef_order%d' %i, 'den_logcoef_order%d' %i, def_den_logcoef[0], def_den_logcoef[1], def_den_logcoef[2] )
                ROOT.SetOwnership(var_den_locoef, False)
                #var.SetName( '%s_order%d' %( self.func_name, i ) )
                arg_list.add( var_den_locoef  ) 

        if self.func_name == 'power' : 
            for i in range( 1, self.func_norders+1 ) :
                this_def_coef = self.get_vals( self.func_name+'_coef', i )
                this_def_pow  = self.get_vals( self.func_name+'_pow', i )

                var_coef = ROOT.RooRealVar( 'coef%d' %i, 'coef%d'%i, this_def_coef[0], this_def_coef[1], this_def_coef[2] )
                ROOT.SetOwnership(var_coef, False)
                var_pow = ROOT.RooRealVar( 'pow%d' %i, 'pow%d'%i, this_def_pow[0], this_def_pow[1], this_def_pow[2] )
                ROOT.SetOwnership(var_pow, False)

                arg_list.add( var_coef )
                arg_list.add( var_pow )


    def get_fit_function( self, forceUseRooFit=False ) :

        function = ''

        if self.func_name == 'dijet' : 
            order_entries = []

            log_str = 'TMath::Log10(@0/13000)'
            for i in range( 1, self.func_norders) :
                order_entries.append('@'+str(i+1)+'*' + '*'.join( [log_str]*i))
            
            function = 'TMath::Power( @0/13000., @1 + ' + '+'.join( order_entries) + ')'


        if self.func_name == 'atlas' : 

            function = 'TMath::Power( (1-(@0/13000.)), @1 ) / ( TMath::Power( @0/13000. , @2+ '
            order_entries = []
            for i in range( 0, self.func_norders ) :
                order_entries.append( '@%d*TMath::Log10( @0/13000.)'  %( i+3 ) )

            function += ' + '.join( order_entries )
            function += ' ) )'

        if self.func_name == 'power' : 

            order_entries = []
            for i in range( 0, self.func_norders ) :
                order_entries.append( '@%d*TMath::Power( @0, @%d )'  %( i*2+1, i*2+2 ) )

            function = '+'.join( order_entries )

        if self.useRooFit or forceUseRooFit :
            return function
        else :
            mod_function = function.replace( '@0', 'x' )
            mod_function = '[0]*' + mod_function
            for i in range( 0, 9 ) :
                mod_function = mod_function.replace( '@%d' %i, '[%d]' %i )
            return mod_function

    def fit_histogram(self ) : 

        xmin = self.xvar.getMin()
        xmax = self.xvar.getMax()
    
        if self.useRooFit :

            arg_list = ROOT.RooArgList()
            ROOT.SetOwnership(arg_list, False)
            
            arg_list.add( self.xvar )
            self.add_vars( arg_list)

            func_str = self.get_fit_function() 

            self.func_pdf = ROOT.RooGenericPdf('%s_%s' %(self.func_name, self.label), self.func_name, func_str, arg_list)
            ROOT.SetOwnership(func_pdf, False)

            self.func_pdf.fitTo( self.datahist, ROOT.RooFit.Range( xmin, xmax),ROOT.RooFit.SumW2Error(True)  )

            return func_pdf
        else :

            func_str = self.get_fit_function( ) 

            self.func = ROOT.TF1( 'tf1_%s' %self.label, func_str, xmin, xmax )

            if self.func_name == 'dijet' : 

                self.func.SetParameter( 0, 0.0000001)
                param = 1
                for i in range( 1, self.func_norders+1 ) :
                    this_def = self.get_vals( self.func_name, i )
                    self.func.SetParameter( param, this_def[0] )
                    param += 1
            
            self.hist.Fit( self.func, 'R' )

            return self.func

    def calculate_func_pdf( self ) :

        if self.func_pdf is not None : 
            print 'The PDF Function already exists.  It will be overwritten'
        
        if self.func_name == 'dijet' :
            for i in range( 1, self.func_norders+1 ) :
                fitted_result = self.func.GetParameter(i)
                fitted_error = self.func.GetParError(i)

                self.defs['dijet'][i] = ( fitted_result, fitted_result - fitted_error, fitted_result + fitted_error )

            arg_list = ROOT.RooArgList()
            ROOT.SetOwnership(arg_list, False)
            arg_list.add( self.xvar )
            self.add_vars( arg_list )

            for i in range( 1, arg_list.getSize() )  :
                fitted_error = self.func.GetParError(i)
                arg_list[i].setError( fitted_error )


            func_str = self.get_fit_function( forceUseRooFit=True) 

            self.func_pdf = ROOT.RooGenericPdf('%s_%s' %(self.func_name, self.label), self.func_name, func_str, arg_list)
            ROOT.SetOwnership(self.func_pdf, False)


    def get_defaults( self, sample, var, ieta ) :
    
        self.set_vals('dijet', 1, ( -10.5, -20, 0 ) )
        self.set_vals('dijet', 2, (-2.03, -10, 0) )
        self.set_vals('dijet', 3, ( 0.0, -10, 10) )
        self.set_vals('dijet', 4, (0.0, -10 ,10 ) )
        self.set_vals('dijet', 5, (0.0, -10 ,10 ) )
    
        self.set_vals('power_coef', 1, ( 1000, 0, 10000000 ) )
        self.set_vals('power_coef', 2, (1000, 0, 100000000) )
        self.set_vals('power_coef', 3, ( 0.0, 0, 10) )
        self.set_vals('power_coef', 4, (0.0, 0 ,10 ) )
        self.set_vals('power_coef', 5, (0.0, 0 ,10 ) )
    
        self.set_vals('power_pow', 1, ( -9.9, -100, 100 ) )
        self.set_vals('power_pow', 2, (-0.85, -10, 10) )
        self.set_vals('power_pow', 3, ( 0.0, -10, 10) )
        self.set_vals('power_pow', 4, (0.0, -10 ,10 ) )
        self.set_vals('power_pow', 5, (0.0, -10 ,10 ) )
    
        self.set_vals('atlas_num_power', 1, ( -9.9, -100, 100 ) )
        self.set_vals('atlas_den_power', 1, ( -9.9, -100, 100 ) )
        self.set_vals('atlas_den_logcoef', 1, ( -9.9, -100, 100 ) )
        self.set_vals('atlas_den_logcoef', 2, ( -9.9, -100, 100 ) )
    
    

