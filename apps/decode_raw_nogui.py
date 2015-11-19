#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Decode Raw Nogui
# Generated: Thu Nov 19 04:32:25 2015
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from math import pi
from optparse import OptionParser
import grgsm
import pmt

class decode_raw_nogui(gr.top_block):

    def __init__(self, fc=943.6e6, shiftoff=400e3, ppm=0, gain=30, samp_rate=2000000.052982):
        gr.top_block.__init__(self, "Decode Raw Nogui")

        ##################################################
        # Parameters
        ##################################################
        self.fc = fc
        self.shiftoff = shiftoff
        self.ppm = ppm
        self.gain = gain
        self.samp_rate = samp_rate

        ##################################################
        # Blocks
        ##################################################
        self.gsm_sdcch8_demapper_0 = grgsm.universal_ctrl_chans_demapper(1, ([0,4,8,12,16,20,24,28,32,36,40,44]), ([8,8,8,8,8,8,8,8,136,136,136,136]))
        self.gsm_receiver_0 = grgsm.receiver(4, ([0]), ([]))
        self.gsm_message_printer_1 = grgsm.message_printer(pmt.intern(""), False,
            False, False)
        self.gsm_input_0 = grgsm.gsm_input(
            ppm=0,
            osr=4,
            fc=fc,
            samp_rate_in=samp_rate,
        )
        self.gsm_decryption_0 = grgsm.decryption(([]), 1)
        self.gsm_control_channels_decoder_0_0 = grgsm.control_channels_decoder()
        self.gsm_control_channels_decoder_0 = grgsm.control_channels_decoder()
        self.gsm_clock_offset_control_0 = grgsm.clock_offset_control(fc-shiftoff)
        self.gsm_bcch_ccch_demapper_0 = grgsm.universal_ctrl_chans_demapper(0, ([2,6,12,16,22,26,32,36,42,46]), ([1,2,2,2,2,2,2,2,2,2]))
        self.blocks_socket_pdu_0_0 = blocks.socket_pdu("UDP_SERVER", "127.0.0.1", "4729", 10000, False)
        self.blocks_socket_pdu_0 = blocks.socket_pdu("UDP_CLIENT", "127.0.0.1", "4729", 10000, False)
        self.blocks_rotator_cc_0 = blocks.rotator_cc(-2*pi*shiftoff/samp_rate)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_gr_complex*1, "/tmp/gsm_raw", False)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_rotator_cc_0, 0), (self.gsm_input_0, 0))
        self.connect((self.gsm_input_0, 0), (self.gsm_receiver_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_rotator_cc_0, 0))

        ##################################################
        # Asynch Message Connections
        ##################################################
        self.msg_connect(self.gsm_bcch_ccch_demapper_0, "bursts", self.gsm_control_channels_decoder_0, "bursts")
        self.msg_connect(self.gsm_clock_offset_control_0, "ppm", self.gsm_input_0, "ppm_in")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.blocks_socket_pdu_0, "pdus")
        self.msg_connect(self.gsm_control_channels_decoder_0, "msgs", self.gsm_message_printer_1, "msgs")
        self.msg_connect(self.gsm_control_channels_decoder_0_0, "msgs", self.blocks_socket_pdu_0, "pdus")
        self.msg_connect(self.gsm_control_channels_decoder_0_0, "msgs", self.gsm_message_printer_1, "msgs")
        self.msg_connect(self.gsm_decryption_0, "bursts", self.gsm_control_channels_decoder_0_0, "bursts")
        self.msg_connect(self.gsm_receiver_0, "C0", self.gsm_bcch_ccch_demapper_0, "bursts")
        self.msg_connect(self.gsm_receiver_0, "C0", self.gsm_sdcch8_demapper_0, "bursts")
        self.msg_connect(self.gsm_receiver_0, "measurements", self.gsm_clock_offset_control_0, "measurements")
        self.msg_connect(self.gsm_sdcch8_demapper_0, "bursts", self.gsm_decryption_0, "bursts")


    def get_fc(self):
        return self.fc

    def set_fc(self, fc):
        self.fc = fc
        self.gsm_input_0.set_fc(self.fc)

    def get_shiftoff(self):
        return self.shiftoff

    def set_shiftoff(self, shiftoff):
        self.shiftoff = shiftoff
        self.blocks_rotator_cc_0.set_phase_inc(-2*pi*self.shiftoff/self.samp_rate)

    def get_ppm(self):
        return self.ppm

    def set_ppm(self, ppm):
        self.ppm = ppm

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.gsm_input_0.set_samp_rate_in(self.samp_rate)
        self.blocks_rotator_cc_0.set_phase_inc(-2*pi*self.shiftoff/self.samp_rate)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("-f", "--fc", dest="fc", type="eng_float", default=eng_notation.num_to_str(943.6e6),
        help="Set fc [default=%default]")
    parser.add_option("-o", "--shiftoff", dest="shiftoff", type="eng_float", default=eng_notation.num_to_str(400e3),
        help="Set shiftoff [default=%default]")
    parser.add_option("-p", "--ppm", dest="ppm", type="intx", default=0,
        help="Set ppm [default=%default]")
    parser.add_option("-g", "--gain", dest="gain", type="eng_float", default=eng_notation.num_to_str(30),
        help="Set gain [default=%default]")
    parser.add_option("-s", "--samp-rate", dest="samp_rate", type="eng_float", default=eng_notation.num_to_str(2000000.052982),
        help="Set samp_rate [default=%default]")
    (options, args) = parser.parse_args()
    tb = decode_raw_nogui(fc=options.fc, shiftoff=options.shiftoff, ppm=options.ppm, gain=options.gain, samp_rate=options.samp_rate)
    tb.start()
    tb.wait()
